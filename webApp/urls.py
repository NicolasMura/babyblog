# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^', include('babyblog.urls', namespace='babyblog')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^user/', include('zn_users.urls', namespace='zn_users')),
    url(r'^admin/', include(admin.site.urls)),
    # url(
    #     r'^api/',
    #     include('babyblog.api_v1_0.urls', namespace='api_v1_0')
    # ),
)

urlpatterns += (
    url(
        r'^m/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(
        r'^s/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
)
