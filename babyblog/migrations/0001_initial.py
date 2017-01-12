# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import babyblog.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=255)),
                ('likes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='upload/images', null=True, verbose_name='Votre image', validators=[babyblog.models.validate_image])),
                ('parent', models.ForeignKey(blank=True, to='babyblog.Post', null=True)),
                ('user', models.ForeignKey(related_name='posts', default='', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
