# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
# from django.contrib.sites.models import Site  # utile ?
# from django.utils.encoding import python_2_unicode_compatible  # utile ?


POST_TITLE_MAX_LENGTH = 200
COMMENT_MAX_LENGTH = 1000

VALID_IMG_EXTENSIONS = [
        ".jpg", ".JPG",
        ".jpeg", ".JPEG",
        ".png", ".PNG",
        ".gif", ".GIF",
    ]
MEGABYTE_LIMIT = 2
MAX_WIDTH = 6000
MAX_HEIGHT = 6000


def validate_image(
        fieldfile_obj,
        max_width=MAX_WIDTH,
        max_height=MAX_HEIGHT,
        max_size=MEGABYTE_LIMIT*1024*1024,
        valid_extensions=VALID_IMG_EXTENSIONS):
    # Below condition is for robustness only
    if not fieldfile_obj.file.name.endswith(tuple(VALID_IMG_EXTENSIONS)):
            raise ValidationError(_(
                "Erreur : le format de l'image est incorrect ! "
                "(Formats autorisés : {})".format(VALID_IMG_EXTENSIONS)))
    if hasattr(fieldfile_obj.file, 'image'):
        if (
            fieldfile_obj.file.image.width > max_width or
            fieldfile_obj.file.image.height > max_height
        ):
            raise ValidationError(_(
                "Erreur : les dimensions de l'image excèdent le maximum "
                "autorisé ({} x {} max).").format(MAX_WIDTH, MAX_HEIGHT))
        img_width = fieldfile_obj.file.image.size[0]
        img_height = fieldfile_obj.file.image.size[1]
        if img_width*img_height > max_size:
            raise ValidationError(_(
                "L'image dépasse la taille maximale "
                "autorisée ({} Mo)".format(MEGABYTE_LIMIT)))


# @python_2_unicode_compatible
class PostCommentAbstract(models.Model):
    """
    A user post/comment about some object.
    """

    class Meta:
        abstract = True
        ordering = ('submit_date', )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Auteur'),
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        related_name="%(class)s_author",
        # on_delete=models.SET_NULL,
    )
    content = models.TextField(
        verbose_name=_('Contenu'),
        max_length=COMMENT_MAX_LENGTH,
        default="",
        blank=False,
    )
    # Metadata about the post/comment
    submit_date = models.DateTimeField(
        verbose_name=_('Date de publication'),
        auto_now_add=True,
        auto_now=False,
    )
    is_public = models.BooleanField(
        verbose_name=_('publique ?'),
        default=True,
        help_text=_(
            'Uncheck this box to make the comment effectively '
            'disappear from the site.'
        ),
    )
    is_removed = models.BooleanField(
        verbose_name=_('Désactivé ?'),
        default=False,
        help_text=_(
            'Check this box if the comment is inappropriate. '
            'A "This comment has been removed" message will '
            'be displayed instead.'
        ),
    )

    # def get_absolute_url(self, anchor_pattern="#c%(id)s"):
    #     return self.get_content_object_url() + (
    #         anchor_pattern % self.__dict__)

    def get_as_text(self):
        """
        Return this comment as plain text. Useful for emails.
        """
        d = {
            'profile': self.profile,
            'date': self.submit_date,
            'comment': self.comment,
            'domain': self.site.domain,
        }
        return _(
            'Posted by %(profile)s '
            'at %(date)s\n\n%(comment)s\n\nhttp://%(domain)s'
        ) % d


class Post(PostCommentAbstract):
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    title = models.CharField(
        verbose_name=_('Titre'),
        max_length=POST_TITLE_MAX_LENGTH,
        default='',
        blank=False,
    )
    slug = models.SlugField(
        unique=True,
    )
    image = models.ImageField(
        verbose_name=_("Votre image"),
        blank=True,
        null=False,
        upload_to='upload/images',
        validators=[validate_image],
    )

    def __unicode__(self):
        return _("Post de %(author)s : %(content)s...") % {
            'author': self.author, 'content': self.content[:50]}

    # @models.permalink
    # def get_absolute_url(self):
    #     return (
    #         'blog_post_detail',
    #         (),
    #         {
    #             'slug': self.slug,
    #         })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(PostCommentAbstract):
    class Meta:
        verbose_name = _('Commentaire')
        verbose_name_plural = _('Commentaires')

    related_post = models.ForeignKey(
        'babyblog.Post',
        verbose_name=_('Post relatif'),
        blank=False,
        null=False,
        # related_name="%(class)s_comments",
        # on_delete=models.SET_NULL,
        # related_name="wall",
        )

    def __unicode__(self):
        return _("Commentaire de %(author)s : %(content)s...") % {
            'author': self.author, 'content': self.content[:50]}
