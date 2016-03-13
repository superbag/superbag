# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160104_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=10000)),
                ('language', models.CharField(max_length=5)),
            ],
        ),
    ]
