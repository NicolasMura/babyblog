# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View

from models import Post
# from forms import PostForm


def home(request):
    if not request.user.is_authenticated():
        return redirect(reverse_lazy('zn_auth:login'))


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


class HomeView(ListView, View):
    """
    TO WRITE
    """
    model = Post
    queryset = Post.objects.order_by('-date')
    template_name = "babyblog/blog_list.html"

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(IndexView, self).dispatch(request, *args, **kwargs)

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


# class SingleBlog(AppView):
#     """
#     TO WRITE
#     """
#     template_name = "babyblog/single_blog.html"

#     def get(self, request, slug):
#         post = get_object_or_404(Post, slug=slug)
#         self.context.update({
#             'post': post,
#             })
#         return render(request, self.template_name, self.context)

#     def post(self, request):
#         form = PostForm(request.POST or None)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return render(request, self.template_name, self.context)
#         return render(request, self.template_name, self.context)

#     def render(self, request):
#         return render(request, self.template_name, self.context)


class SingleBlog(DetailView):
    """
    TO WRITE
    """
    template_name = "babyblog/single_blog.html"
    model = Post


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
