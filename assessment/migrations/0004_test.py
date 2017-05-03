# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_course_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_title', models.CharField(max_length=50)),
                ('question_1', models.CharField(max_length=1000)),
                ('answer_1', models.CharField(max_length=1000)),
                ('question_2', models.CharField(max_length=1000)),
                ('answer_2', models.CharField(max_length=1000)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.Course')),
            ],
        ),
    ]
