# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-20 16:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0006_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 16, 14, 54, 805486, tzinfo=utc)),
        ),
    ]
