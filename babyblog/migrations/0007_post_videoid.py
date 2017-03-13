# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyblog', '0006_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videoId',
            field=models.TextField(default='', max_length=100, blank=True),
        ),
    ]
