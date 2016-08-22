# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import exceptions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=exceptions.FutureWarning)),
                ('price', models.DecimalField(decimal_places=2, default=29.99, max_digits=100)),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
