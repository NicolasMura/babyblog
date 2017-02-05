# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns(
    '',
    # REST API's urls
    url(
        r'^$',
        views.api_root,
    ),
    url(
        r'^posts$',
        views.PostAPIViewSet.as_view({'get': 'list'}),
        name='post-list',
    ),
    url(
        r'^posts/create$',
        views.PostCreateAPIView.as_view(),
        name='post-create',
    ),
    url(
        r'^posts/(?P<pk>[0-9]+)/$',
        views.PostDetailAPIView.as_view(),
        name='post-detail',
    ),
    url(
        r'^posts/latest$',
        views.PostLatestDetailAPIView.as_view(),
        name='post-latest-detail',
    ),
    url(
        r'^users$',
        views.UserListAPIView.as_view(),
        name='user-list',
    ),
    url(
        r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetailAPIView.as_view(),
        name='user-detail',
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
