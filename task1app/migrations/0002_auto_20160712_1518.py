# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_title',
            field=models.CharField(default='__str__', max_length=50),
        ),
        migrations.AddField(
            model_name='question',
            name='question_title',
            field=models.CharField(default='__str__', max_length=50),
        ),
    ]
