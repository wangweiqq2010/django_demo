# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-30 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='math',
            name='score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='math',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='introduction',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='join_date',
            field=models.DateField(null=True),
        ),
    ]
