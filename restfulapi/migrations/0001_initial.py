# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=200)),
                ('studentid', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('github', models.CharField(max_length=20)),
                ('web', models.CharField(max_length=20)),
            ],
        ),
    ]
