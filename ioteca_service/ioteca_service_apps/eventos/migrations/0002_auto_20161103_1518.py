# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-03 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asistencia',
            options={'verbose_name': 'Asistencia', 'verbose_name_plural': 'Asistencias'},
        ),
        migrations.AlterModelOptions(
            name='inasistencia',
            options={'verbose_name': 'Inasistencia', 'verbose_name_plural': 'Inasistencias'},
        ),
        migrations.RemoveField(
            model_name='inasistencia',
            name='fecha',
        ),
    ]
