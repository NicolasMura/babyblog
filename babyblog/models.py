# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


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


class Post(models.Model):
    class Meta:
        ordering = ('date', )

    user = models.ForeignKey(
        User,
        related_name='posts',
        # max_length=COMMENT_MAX_LENGTH,
        default="",
        blank=False,
    )
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)
    parent = models.ForeignKey(
        'self',
        related_name='reply_set',
        null=True,
        blank=True
    )
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    image = models.ImageField(
        verbose_name=_("Votre image"),
        blank=True,
        null=True,
        upload_to='upload/images',
        validators=[validate_image],
    )
    link = models.URLField(
        max_length=200,
        blank=True,
        default="",
    )
    videoUrl = models.URLField(
        max_length=200,
        blank=True,
        default="",
    )

    def __unicode__(self):
        return _("Post de %(user)s : %(content)s...") % {
            'user': self.user.username, 'content': self.content[:50]}

    def get_comments(self):
        return Post.objects.filter(parent=self).order_by('date')

    def get_comments_number(self):
        return Post.objects.filter(parent=self).count()

    def get_first_letter(self):
        return "{}".format(self.content[:1])

    def without_first_letter(self):
        return "{}".format(self.content[1:])
