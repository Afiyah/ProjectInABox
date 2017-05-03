# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-26 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotly', '0005_course_course_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_embed',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
