# Generated by Django 2.2.4 on 2019-08-17 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApplication', '0013_auto_20190817_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogApplication.Category'),
        ),
    ]
