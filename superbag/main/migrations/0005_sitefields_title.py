# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_sitefields'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitefields',
            name='title',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
