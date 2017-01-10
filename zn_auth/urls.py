# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

urlpatterns = patterns(
    '',
    url(
        r'^login',
        auth_views.login,
        {'template_name': 'zn_auth/login.html'},
        name='login',
    ),
)
