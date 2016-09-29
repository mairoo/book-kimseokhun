# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'verbose_name': 'Bookmark', 'verbose_name_plural': 'Bookmarks'},
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='url',
            field=models.URLField(unique=True, verbose_name='URL'),
        ),
    ]