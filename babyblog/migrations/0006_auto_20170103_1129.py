# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyblog', '0005_auto_20170103_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='', max_length=1000, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='', max_length=1000, verbose_name='Contenu'),
        ),
    ]
