# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_albums', '0003_auto_20160121_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active?'),
        ),
        migrations.AddField(
            model_name='artist',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active?'),
        ),
        migrations.AddField(
            model_name='label',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active?'),
        ),
    ]
