# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-03 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventos', '0005_auto_20161103_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('imagen', models.ImageField(upload_to='')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('num_recibo', models.CharField(max_length=50)),
                ('validacion', models.BooleanField(default=False)),
                ('inasistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
            ],
            options={
                'verbose_name_plural': 'Pagos',
                'verbose_name': 'Pago',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Periodos',
                'verbose_name': 'Periodo',
            },
        ),
        migrations.AddField(
            model_name='pago',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagos.Periodo'),
        ),
    ]