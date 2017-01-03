# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
# from django.utils.html import strip_tags (TO DO)

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'slug']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['related_post']
