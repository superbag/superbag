# -*- coding: utf-8 -*-

import datetime

from django.db import models


class SalePoint(models.Model):
    TYPE_CHOICES = (
        ('air', 'airport'),
        ('tr', 'train station'),
        ('bus', 'bus station'),
    )

    lon = models.FloatField(null=False, blank=False)
    lat = models.FloatField(null=False, blank=False)
    name = models.CharField(max_length=256, null=False, blank=False)
    address = models.CharField(max_length=512, null=False, blank=False)
    point_type = models.CharField(
        max_length=64, null=False, blank=False, choices=TYPE_CHOICES)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=256, blank=False)
    email = models.CharField(max_length=256, blank=False)
    text = models.CharField(max_length=4096, blank=False)
    created = models.DateField(default=datetime.datetime.now)

    def __unicode__(self):
        return u'{} {}'.format(self.name, self.email)


class InsuranceRequest(models.Model):
    author = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    email = models.EmailField(max_length=256)
    airport_arrival = models.CharField(max_length=256)
    airport_destination = models.CharField(max_length=256)
    ticket_num = models.CharField(max_length=32)
    created = models.DateField(default=datetime.datetime.now)
    event_date = models.DateField()
    description = models.CharField(max_length=2056)
    info = models.CharField(max_length=2056, blank=True)

    def __unicode__(self):
        return u'{} в {}'.format(self.author, self.event_date)


class SiteFields(models.Model):
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=10000)
    language = models.CharField(max_length=5)

    def __unicode__(self):
        return u'{} {}'.format(self.language, self.title)
