# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-21 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0005_auto_20160921_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogApplication.Category'),
        ),
    ]