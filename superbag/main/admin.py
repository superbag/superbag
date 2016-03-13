# -*- coding: utf-8 -*-

from django.contrib import admin
# from leaflet.admin import LeafletGeoAdmin

from .models import SalePoint, Contact, InsuranceRequest, SiteFields


admin.site.register(SalePoint)
admin.site.register(InsuranceRequest)
admin.site.register(SiteFields)


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['name', 'email', 'text']


# @admin.register(SalePoint)
# class SalePoint(admin.ModelAdmin):
#     list_display = [
#         'name',
#         'address',
#         'point_type',
#         'lon',
#         'lat',
#     ]
