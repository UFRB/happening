# -*- coding: utf-8 -*-
from django.contrib.admin import ModelAdmin
from django.contrib import admin

from .models import Event, Discipline, City


class EventAdmin(ModelAdmin):
    date_hierarchy = 'starts'
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'venue', 'starts')
    list_filter = ('starts', 'city', 'venue', 'discipline')


class DisciplineAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CityAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'state')


admin.site.register(Event, EventAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(City, CityAdmin)