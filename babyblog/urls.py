# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
import views

urlpatterns = patterns(
    '',
    url(
        r'^$',
        # login_required(views.HomeView.as_view()),
        views.HomeView.as_view(),
        name='home',
    ),
    url(
        r'^gallery$',
        views.HomeView2.as_view(),
        name='home2',
    ),
    url(
        r'^post/(?P<pk>\d+)$',
        views.SingleBlog.as_view(),
        name='post',
    ),
    url(
        r'^post-slider$',
        views.SingleBlogSlider.as_view(),
        name='post-slider',
    ),
    url(
        r'^post-video$',
        views.SingleBlogVideo.as_view(),
        name='post-video',
    ),
    # url(
    #     r'^submit-comment$',
    #     views.submit_comment,
    #     name='submit-comment',
    # )
)
