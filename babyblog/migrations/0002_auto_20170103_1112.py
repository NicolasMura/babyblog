# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='test', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='', max_length=1000, verbose_name='Commentaire'),
        ),
    ]
