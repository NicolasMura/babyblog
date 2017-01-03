# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyblog', '0004_auto_20170103_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(default='', max_length=1000, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='', max_length=1000, verbose_name='Contenu'),
        ),
    ]
