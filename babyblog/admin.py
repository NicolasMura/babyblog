# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        # 'user',
        'date',
        'preview',
    )

    fieldsets = (
        (
            _('Contenu'),
            {'fields': ('user', 'parent', 'content',
                        'link', 'image', 'videoUrl')}
        ),
        # (
        #     _('Metadata'),
        #     {'fields': ('date', )}
        # ),
    )

    list_filter = ('date', )
    date_hierarchy = 'date'
    ordering = ('-date',)
    search_fields = ('content', )
    # search_fields = ('content', 'user')

    def preview(self, post):
        if len(post.content) > 50:
            return "{}...".format(post.content[:50])

        return post.content

    preview.short_description = 'Aperçu du post'


admin.site.register(Post, PostAdmin)
