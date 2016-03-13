# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_insurancerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='insurancerequest',
            name='email',
            field=models.EmailField(max_length=256),
        ),
        migrations.AlterField(
            model_name='insurancerequest',
            name='info',
            field=models.CharField(max_length=2056, blank=True),
        ),
    ]
