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
        fields = ('id', 'username', 'email', 'profile_avatar_url')
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


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user = UserSerializer()
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    parent = serializers.StringRelatedField(many=False)
    # reply_set = RecursiveField(many=True)  # marche pas
    # related_comments = serializers.SerializerMethodField()
    image = Base64ImageField(
        max_length=None, use_url=True,
        allow_empty_file=True, required=False, )

    class Meta:
        model = Post
        fields = ('id', 'user', 'date', 'content',
                  'parent', 'likes', 'comments', 'image')
        # depth = 1

    def create(self, validated_data):
        print('validated_data : ', validated_data)

        content = validated_data['content']
        print('content : ', content)
        image = validated_data['image']
        print('image : ', image)

        username = validated_data['user']['username']
        print('username : ', username)

        user = User.objects.get(username=username)
        print('repr(user) : ', repr(user))

        post = Post.objects.create(
            user=user,
            content=content,
            image=image,
        )

        return post

    # # TEST https://medium.com/django-rest-framework/dealing-with-unique-
    # # constraints-in-nested-serializers-dade33b831d9#.x1x1jxn0y
    # def create(self, validated_data):
    #     owner_data = validated_data.pop('user')
    #     username = owner_data.pop('username')
    #     user = get_user_model().objects.get_or_create(username=username)[0]
    #     post = Post.objects.create(user=user, **validated_data)
    #     return post

    # def update(self, instance, validated_data):
    #     owner_data = validated_data.pop('user')
    #     username = owner_data.pop('username')
    #     user = get_user_model().objects.get_or_create(username=username)[0]
    #     instance.user = user
    #     instance.name = validated_data['name']
    #     return instance

    # Marche pas
    # def get_related_comments(self, obj):
    #     return Post.objects.filter(parent=obj)

    # TEST http://stackoverflow.com/questions/33764314/how-can-i-add-
    # a-car-to-a-user-with-django-rest-framework
    # def create(self, validated_data):
    #     """ Add post to an user
    #     """
    #     print(validated_data)
    #     content = validated_data.pop('content')
    #     username = validated_data.pop('username')
    #     parent = None
    #     # image = validated_data.pop('image')
    #     user = User.objects.get(username=username)
    #     post = Post.objects.create(
    #         user=user,
    #         parent=parent,
    #         content=content,
    #         # image=image,
    #     )

    #     return post


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    parent = serializers.StringRelatedField(many=False)
    # reply_set = RecursiveField(many=True)  # marche pas
    # related_comments = serializers.SerializerMethodField()
    # image = Base64ImageField(
    #     max_length=None, use_url=True,
    #     allow_empty_file=True, required=False, )

    class Meta:
        model = Post
        fields = ('user', 'date', 'content',
                  'parent', 'likes', 'comments', 'image')

    # def get_related_comments(self, obj):
    #     return Post.objects.filter(parent=obj)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content', 'image')

    # def get_related_comments(self, obj):
    #     return Post.objects.filter(parent=obj)


class PostCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    post = PostSerializer()

    class Meta:
        fields = ('username', 'post')

    def create(self, validated_data):
        print(validated_data)
        tmp_post = validated_data.pop('post')
        user = User.objects.get(username=validated_data['username'])
        post = Post.objects.create(
            user=user,
            content=tmp_post['content'],
            image=tmp_post['image'],
        )

        return post
