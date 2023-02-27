# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-02-27 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milalfriend',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='graduation_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
