# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from models import Post
from forms import PostForm


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
