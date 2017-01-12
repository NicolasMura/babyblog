# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyblog', '0004_post_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(related_name='reply_set', blank=True, to='babyblog.Post', null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
