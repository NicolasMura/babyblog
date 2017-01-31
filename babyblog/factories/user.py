# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from zn_auth.models import Profile
import factory
import factory.fuzzy
# from django.db.models.signals import post_save


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('first_name')
    # We pass in 'user' to link the generated Profile to our
    # just-generated User
    # This will call ProfileFactory(user=our_new_user), thus skipping the
    # SubFactory.

    # @classmethod
    # def _generate(cls, create, attrs):
    #     """Override the default _generate() to disable the post-save signal."""

    #     # Note: If the signal was defined with a dispatch_uid, include that
    #     # in both calls.
    #     post_save.disconnect(handler_create_user_profile, User)
    #     user = super(UserFactory, cls)._generate(create, attrs)
    #     post_save.connect(handler_create_user_profile, User)
    #     return user


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    # We pass in profile=None to prevent UserFactory from creating
    # another profile (this disables the RelatedFactory)
    user = factory.SubFactory(UserFactory, profile=None)
    avatar = factory.django.ImageField()
    # avatar = factory.Faker('image_url', width=None, height=None)
