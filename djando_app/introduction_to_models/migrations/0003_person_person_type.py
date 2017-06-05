# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0002_auto_20170605_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_type',
            field=models.CharField(choices=[('student', '학생'), ('tescher', '선생')], default='student', max_length=10, verbose_name='유형'),
        ),
    ]