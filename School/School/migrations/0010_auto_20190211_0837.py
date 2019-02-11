# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-11 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0009_remove_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='School.Student'),
        ),
    ]
