# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-26 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_course_course_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
