# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Post
from forms import PostForm
from serializers import (
    PostSerializer,
    ProfileSerializer,
)
from rest_framework import generics
# from rest_framework import permissions
# from snippets.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrCreate

# Imports for endpoint for the root of our ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# Imports for oauth2_provider
# from oauth2_provider.ext.rest_framework import OAuth2Authentication

# Test
from rest_framework.parsers import MultiPartParser, JSONParser
# from rest_framework.parsers import MultiPartParser, FileUploadParser, JSONParser, FormParser


from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from zn_users.models import Profile


# REST views
# Endpoint for the root of our ListAPIView
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'profiles': reverse(
            'babyblog:profile-list', request=request, format=format),
        'posts': reverse(
            'babyblog:post-list', request=request, format=format)
    })


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = [OAuth2Authentication]
    # permission_classes = [TokenHasScope]
    # parser_classes = (MultiPartParser, FileUploadParser, JSONParser, FormParser)
    parser_classes = (MultiPartParser, JSONParser)

    # # Overriding .perform_create() method to associate Snippets with Users
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrReadOnly,
    # )


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# Classic views
class AppView(View):
    """
    Base view for ZuokiN's blog views
    """
    def __init__(self, *args, **kwargs):
        self.context = {}
        return super(AppView, self).__init__(*args, **kwargs)

    def get(self, request):
        return self.render(request)

    def render(self, request):
        return render(request, self.template_name, self.context)


class HomeView(ListView):
    """
    TO WRITE
    """
    model = Post
    template_name = "babyblog/blog_list.html"

    # def get(self, request):
    #     return render(request, self.template_name, self.context)

    # def render(self, request):
    #     return render(request, self.template_name, self.context)


class HomeView2(AppView):
    """
    TO WRITE
    """
    template_name = "babyblog/blog_gallery.html"

    def get(self, request):
        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)


class SingleBlog(AppView):
    """
    TO WRITE
    """
    template_name = "babyblog/single_blog.html"

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        self.context.update({
            'post': post,
            })
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, self.template_name, self.context)
        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)


class SingleBlogSlider(AppView):
    """
    TO WRITE
    """
    template_name = "babyblog/single_blog_slider.html"

    def get(self, request):
        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)


class SingleBlogVideo(AppView):
    """
    TO WRITE
    """
    template_name = "babyblog/single_blog_video.html"

    def get(self, request):
        return render(request, self.template_name, self.context)

    def render(self, request):
        return render(request, self.template_name, self.context)
