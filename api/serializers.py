# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from babyblog.models import Post
from zn_auth.models import Profile
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    avatar = Base64ImageField(
        max_length=None, use_url=True,
        allow_empty_file=True, required=False, )

    class Meta:
        model = Profile
        fields = ('id', 'user', 'avatar', 'username', 'email',
                  'first_name', 'last_name')

    def get_username(self, object):
        return object.user.username

    def get_email(self, object):
        return object.user.email

    def get_first_name(self, object):
        return object.user.first_name

    def get_last_name(self, object):
        return object.user.last_name


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile')


# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False)
#     parent = serializers.StringRelatedField(many=False)
#     # image = Base64ImageField(
#     #     max_length=None, use_url=True,
#     #     allow_empty_file=True, required=False, )

#     class Meta:
#         model = Post
#         # fields = ('user', 'date', 'content', 'parent', 'likes', 'comments')
#         fields = ('user', 'date', 'content', 'parent', 'likes')


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    parent = serializers.StringRelatedField(many=False)
    reply_set = RecursiveSerializer(many=True, read_only=True)  # marche pas
    # image = Base64ImageField(
    #     max_length=None, use_url=True,
    #     allow_empty_file=True, required=False, )

    class Meta:
        model = Post
        fields = ('user', 'date', 'content',
                  'parent', 'likes', 'comments', 'image', 'reply_set')

    def get_comments(self, obj):
        return self.object.all.filter(parent=self).order_by('date')
