# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('img', models.CharField(max_length=400)),
                ('rental_type', models.CharField(max_length=400)),
                ('rent_val', models.CharField(max_length=400)),
                ('rep_val', models.CharField(max_length=400)),
            ],
        ),
    ]
