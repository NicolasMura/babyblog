# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyblog', '0008_auto_20170313_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='videoId',
        ),
        migrations.AddField(
            model_name='post',
            name='videoUrl',
            field=models.URLField(default='', max_length=100, blank=True),
        ),
    ]
