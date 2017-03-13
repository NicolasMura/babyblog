# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyblog', '0009_auto_20170313_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='videoUrl',
            field=models.URLField(default='', blank=True),
        ),
    ]
