# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0002_auto_20170814_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('area', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='choide',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Poll'),
        ),
    ]