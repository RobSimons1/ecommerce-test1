# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-07-15 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_ratings', '0002_auto_20210715_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='3', max_length=10),
        ),
    ]