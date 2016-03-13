# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=256)),
                ('airport_arrival', models.CharField(max_length=256)),
                ('airport_destination', models.CharField(max_length=256)),
                ('ticket_num', models.CharField(max_length=32)),
                ('created', models.DateField(default=datetime.datetime.now)),
                ('event_date', models.DateField()),
                ('description', models.CharField(max_length=2056)),
                ('info', models.CharField(max_length=2056)),
            ],
        ),
    ]
