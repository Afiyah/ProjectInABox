# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-18 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0007_remove_test_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assessment.Course'),
            preserve_default=False,
        ),
    ]
