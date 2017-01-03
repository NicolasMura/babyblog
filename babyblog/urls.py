# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns(
    '',
    url(
        r'^$',
        HomeView.as_view(),
        name='home',
    ),
    # url(
    #     r'^archive/month/(?P<year>\d+)/(?P<month>\w+)$',
    #     'django.views.generic.date_based.archive_month',
    #     {
    #         'queryset': Post.objects.all(),
    #         'date_field': 'created_on',
    #     },
    #     name='blog_archive_month',
    # ),
    url(
        r'^gallery$',
        HomeView2.as_view(),
        name='home2',
    ),
    url(
        r'^post$',
        SingleBlog.as_view(),
        name='post',
    ),
    url(
        r'^post-slider$',
        SingleBlogSlider.as_view(),
        name='post-slider',
    ),
    url(
        r'^post-video$',
        SingleBlogVideo.as_view(),
        name='post-video',
    ),
)
