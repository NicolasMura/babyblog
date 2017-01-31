# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', )
    verbose_name = _('Profil utilisateur')
    verbose_name_plural = _('Profils utilisateurs')


admin.site.register(Profile, ProfileAdmin)
