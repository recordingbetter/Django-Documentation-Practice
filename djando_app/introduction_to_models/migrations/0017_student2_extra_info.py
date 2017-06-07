# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0016_commoninfo2_student2_teacher2'),
    ]

    operations = [
        migrations.AddField(
            model_name='student2',
            name='extra_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extra_students', to='introduction_to_models.CommonInfo2'),
        ),
    ]
