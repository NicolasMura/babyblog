# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns(
    '',
    # REST urls
    url(
        r'^api$',
        views.api_root,
    ),
    url(
        r'^api/post-list$',
        views.PostList.as_view(),
        name='post-list',
    ),
    url(
        r'^api/profile-list$',
        views.ProfileList.as_view(),
        name='profile-list',
    ),

    # App urls
    url(
        r'^$',
        views.HomeView.as_view(),
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
        views.HomeView2.as_view(),
        name='home2',
    ),
    url(
        r'^post$',
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
)

urlpatterns = format_suffix_patterns(urlpatterns)

# Login and logout views for the browsable API
urlpatterns += [
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
        # Tip : namespace is optional since Django 1.9+
    ),
]
