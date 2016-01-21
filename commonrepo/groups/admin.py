# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import Group

class GroupAdmin(VersionAdmin):
    fieldsets = [
        ('Group Info',       {'fields': ['name', 'fullname', 'creator', 'logo', 'description']}),
    ]
    
admin.site.register(Group, GroupAdmin)
