# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Group

class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Group Info',       {'fields': ['name', 'fullname', 'creator',]}),
    ]
    
admin.site.register(Group, GroupAdmin)
