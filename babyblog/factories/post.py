# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from .mixins import make_auto_now_date_factory_mixin
from .user import UserFactory
from babyblog.models import Post
import factory
import factory.fuzzy
import datetime
import urllib
from random import randint


PHOTO_FORMATS = [
    ('landscape_LG_G3', {
        'width': 1920,
        'height': 1080,
    }),
    ('portrait_LG_G3', {
        'width': 1080,
        'height': 1920,
    }),
    # TODO : iPhone 6 SE
]


class PostFactory(
        make_auto_now_date_factory_mixin(
            kwargs_date_names=("date", )),
        factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    # user = factory.SubFactory(UserFactory)
    # user = User.objects.get(username='test')
    # date = factory.Faker('date')
    # date = factory.fuzzy.FuzzyNaiveDateTime(datetime.datetime(2016, 1, 1))
    # date = factory.Faker(
    #     'date_time_this_year', before_now=True, after_now=False, tzinfo=None)
    content = factory.Faker('text', max_nb_chars=200)
    parent = None
    likes = 0
    comments = 0

    @factory.post_generation
    def image(self, create, extracted, **kwargs):
        # Get random ratio for image
        random_int = randint(0, len(PHOTO_FORMATS) - 1)
        random_width = PHOTO_FORMATS[random_int][1]['width']
        random_height = PHOTO_FORMATS[random_int][1]['height']
        # Get image from lorempixel.com and save it to upload folder
        urllib.urlretrieve(
            'http://lorempixel.com/' + str(
                random_width) + '/' + str(
                random_height) + '/',
            'media/upload/images/fake-image-' + str(self.id) + '.jpg')
        # Set saved image for new post
        self.image = 'upload/images/fake-image-' + str(self.id) + '.jpg'


# class CommentFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Post

#     user = factory.SubFactory(UserFactory)
#     # date = factory.Faker('date')
#     date = factory.fuzzy.FuzzyNaiveDateTime(datetime.datetime(2016, 1, 1))
#     content = factory.Faker('text', max_nb_chars=100)
#     parent = factory.SubFactory(PostFactory)
#     likes = 0
#     comments = 0
#     image = None


# class Post(models.Model):
#     class Meta:
#         ordering = ('date', )

#     user = models.ForeignKey(
#         User,
#         related_name='posts',
#         # max_length=COMMENT_MAX_LENGTH,
#         default="",
#         blank=False,
#     )
#     date = models.DateTimeField(auto_now_add=True)
#     content = models.TextField(max_length=255, )
#     parent = models.ForeignKey(
#         'self', related_name='reply_set', null=True, blank=True)
#     likes = models.IntegerField(default=0)
#     comments = models.IntegerField(default=0)
#     image = models.ImageField(
#         verbose_name=_("Votre image"),
#         blank=True,
#         null=True,
#         upload_to='upload/images',
#         validators=[validate_image],
