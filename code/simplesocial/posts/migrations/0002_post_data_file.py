# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='data_file',
            field=models.FileField(blank=True, upload_to='joe'),
        ),
    ]