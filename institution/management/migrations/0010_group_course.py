# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-06 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20190505_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.Courses', verbose_name='Course'),
            preserve_default=False,
        ),
    ]
