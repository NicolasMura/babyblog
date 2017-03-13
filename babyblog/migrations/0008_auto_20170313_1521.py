# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyblog', '0007_post_videoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='videoId',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
    ]
