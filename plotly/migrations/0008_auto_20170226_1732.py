# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-26 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotly', '0007_remove_course_course_embed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.CharField(max_length=250),
        ),
    ]
