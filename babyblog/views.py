# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import View

from models import Post
from forms import CommentForm
from django.contrib.auth.models import User
from django.contrib import messages
# from forms import PostForm


def home(request):
    # if not request.user.is_authenticated():
    #     return redirect(reverse_lazy('zn_auth:login'))
    pass


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
    queryset = Post.objects.order_by('-date').filter(parent=None)
    template_name = "babyblog/blog_list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all users
        context['user_list'] = User.objects.all()
        return context

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
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SingleBlog, self).get_context_data(**kwargs)
        # Add in a QuerySet of all users
        context['user_list'] = User.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object)
        print(request.POST)
        new_post = Post.objects.create(
            user=request.user,
            content=request.POST['content'],
            parent=self.object,
        )
        new_post.save()
        self.context = super(SingleBlog, self).get_context_data(**kwargs)
        # Add success message
        messages.add_message(
            request,
            messages.SUCCESS,
            _('Merci pour votre commentaire !')
        )
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
