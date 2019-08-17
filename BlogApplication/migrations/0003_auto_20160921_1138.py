# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-21 11:38
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0002_auto_20160919_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('content', ckeditor.fields.RichTextField(null=True)),
                ('keywords', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('seo_url', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL : (Auto)')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='category_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogApplication.Category'),
        ),
    ]