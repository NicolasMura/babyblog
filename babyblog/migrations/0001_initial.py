# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import babyblog.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submit_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('is_public', models.BooleanField(default=True, help_text='Uncheck this box to make the comment effectively disappear from the site.', verbose_name='publique ?')),
                ('is_removed', models.BooleanField(default=False, help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', verbose_name='D\xe9sactiv\xe9 ?')),
                ('content', models.CharField(default='', max_length=1000, verbose_name='Commentaire')),
                ('author', models.ForeignKey(related_name='comment_author', verbose_name='Auteur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submit_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('is_public', models.BooleanField(default=True, help_text='Uncheck this box to make the comment effectively disappear from the site.', verbose_name='publique ?')),
                ('is_removed', models.BooleanField(default=False, help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', verbose_name='D\xe9sactiv\xe9 ?')),
                ('content', models.TextField(default='', max_length=1000, verbose_name='Message')),
                ('image', models.ImageField(blank=True, upload_to='upload/images', verbose_name='Votre image', validators=[babyblog.models.validate_image])),
                ('author', models.ForeignKey(related_name='post_author', verbose_name='Auteur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='related_post',
            field=models.ForeignKey(verbose_name='Post relatif', to='babyblog.Post'),
        ),
    ]
