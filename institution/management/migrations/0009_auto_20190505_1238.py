# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-05 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_assigngroupcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigngroupcomments',
            name='assign_group_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigngroupcomments', to='management.AssignGroupDetail', verbose_name='Assign Group Comments'),
        ),
    ]
