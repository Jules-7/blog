# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=75)),
                ('text', models.TextField(max_length=500, verbose_name=b'comment')),
                ('pub_date', models.DateTimeField(verbose_name=b'date of posting')),
                ('allowed', models.BooleanField(default=False, verbose_name=b'approved by admin')),
                ('like', models.IntegerField(default=0, verbose_name=b'likes')),
                ('post', models.ForeignKey(related_name='comments', verbose_name=b'post', to='blog.Post')),
            ],
            options={
                'verbose_name': 'Comment',
            },
        ),
    ]
