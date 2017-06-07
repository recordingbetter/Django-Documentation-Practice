# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0018_auto_20170607_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='introduction_to_models.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.Post'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='introduction_to_models.User'),
        ),
    ]
