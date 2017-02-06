# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core import validators
from babyblog.models import Post
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField


class UserSerializer(serializers.ModelSerializer):
    profile_avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'profile_avatar_url', 'date_joined', 'is_superuser')
        # Dispo que sur Django >= 10...
        # extra_kwargs = {
        #     'username': {
        #         'validators': [UnicodeUsernameValidator()],
        #     }
        # }
        # Temp workaround
        extra_kwargs = {
            'username': {
                'validators': [],
            }
        }

    def get_profile_avatar_url(self, object):
        return self.context['request'].build_absolute_uri(
            object.profile.avatar.url)


# class UserSerializer(serializers.ModelSerializer):
#     profile_avatar_url = serializers.SerializerMethodField()

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'profile_avatar_url')

#     def get_profile_avatar_url(self, object):
#         return object.profile.avatar.url


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value, context=self.context)
        return serializer.data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'date', 'content', 'link',
                  'parent', 'likes', 'comments', 'image', 'reply_set')


class PostCreateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user = UserSerializer()
    reply_set = RecursiveSerializer(many=True, read_only=True)
    image = Base64ImageField(
        max_length=None, use_url=True,
        allow_empty_file=True, required=False, )

    class Meta:
        model = Post
        fields = ('id', 'user', 'date', 'content', 'link',
                  'parent', 'likes', 'comments', 'image', 'reply_set')

    def create(self, validated_data):
        print('validated_data : ', validated_data)

        content = validated_data['content']
        print('content : ', content)
        if 'link' in validated_data.keys():
            link = validated_data['link']
        else:
            link = ''
        print('link : ', link)
        if 'image' in validated_data.keys():
            image = validated_data['image']
        else:
            image = None
        print('image : ', image)

        if 'parent' in validated_data.keys():
            relatedPostId = validated_data['parent']
            print(relatedPostId)
        else:
            relatedPostId = None
        print('Post parent : ', relatedPostId)

        username = validated_data['user']['username']
        print('username : ', username)

        user = User.objects.get(username=username)
        print('repr(user) : ', repr(user))

        post = Post.objects.create(
            user=user,
            content=content,
            link=link,
            parent=relatedPostId,
            image=image,
        )

        return post


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    # parent = serializers.StringRelatedField(many=False)
    # reply_set = RecursiveField(many=True)  # marche pas
    # related_comments = serializers.SerializerMethodField()
    # image = Base64ImageField(
    #     max_length=None, use_url=True,
    #     allow_empty_file=True, required=False, )

    class Meta:
        model = Post
        fields = ('user', 'date', 'content',
                  'likes', 'comments', 'image')

    # def get_related_comments(self, obj):
    #     return Post.objects.filter(parent=obj)
