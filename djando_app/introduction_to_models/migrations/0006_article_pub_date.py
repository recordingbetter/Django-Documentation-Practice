# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0005_auto_20170605_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
