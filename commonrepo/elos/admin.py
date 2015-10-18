# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import ELO, ELOType

class ELOAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ELO Info',         {'fields': ['name', 'fullname', 'author']}),
        ('ELO Type',         {'fields': ['original_type']}),
        ('ELO Relationship', {'fields': ['parent_elo']}),
    ]
    
admin.site.register(ELO, ELOAdmin)

class ELOTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Type Name',         {'fields': ['name']}),
        ('Type ID',           {'fields': ['type_id']}),
    ]
    
admin.site.register(ELOType, ELOTypeAdmin)