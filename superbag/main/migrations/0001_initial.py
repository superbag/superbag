# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='SalePoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('point_type', models.CharField(max_length=64, choices=[(b'air', b'airport'), (b'tr', b'train station'), (b'bus', b'bus station')])),
            ],
        ),
    ]
