# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-07-05 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0003_auto_20180705_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='is_pulic',
            field=models.BooleanField(default=False),
        ),
    ]