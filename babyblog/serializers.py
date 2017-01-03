# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from models import Post
from zn_users.models import Profile
from drf_extra_fields.fields import Base64ImageField


# Hyperlink model based serializers
class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='profile.username')
    image = Base64ImageField(
        max_length=None, use_url=True, allow_empty_file=True, required=False, )

    class Meta:
        model = Post
        fields = ('author', 'title', 'slug', 'content', 'image', 'is_public',
                  'submit_date', 'is_removed')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(
    #     many=True, view_name='snippet-detail', read_only=True)

    avatar = Base64ImageField(
        max_length=None, use_url=True, allow_empty_file=True, required=False, )

    class Meta:
        model = Profile
        fields = ('id', 'username', 'avatar')
