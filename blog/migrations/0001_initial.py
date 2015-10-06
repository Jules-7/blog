# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'category title')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name=b'slug')),
            ],
            options={
                'ordering': ('slug',),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'post title')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name=b'slug')),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date of posting')),
                ('expire_date', models.DateTimeField(verbose_name=b'date of post expire')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'show post')),
                ('like', models.IntegerField(default=0, verbose_name=b'likes')),
                ('category', models.ForeignKey(related_name='posts', verbose_name=b'category', to='blog.Category')),
                ('user', models.ForeignKey(related_name='posts', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('slug',),
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
