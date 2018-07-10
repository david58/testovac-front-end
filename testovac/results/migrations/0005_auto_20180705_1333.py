# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-05 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_customresultstable_contests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customresultstable',
            name='slug',
            field=models.SlugField(help_text='Serves as part of URL.<br />Must only contain characters "a-zA-Z0-9_-".', primary_key=True, serialize=False),
        ),
    ]