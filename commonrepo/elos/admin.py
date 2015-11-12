# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import ELO, ELOType, ReusabilityTreeNode

class ELOAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ELO Info',         {'fields': ['name', 'fullname', 'author', 'uuid']}),
        ('ELO Metadata',     {'fields': ['original_type']}),
        ('ELO Version',      {'fields': ['version', 'parent_elo', 'parent_elo_uuid', 'parent_elo_version']}),
    ]
    
admin.site.register(ELO, ELOAdmin)

class ELOTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Type Name',         {'fields': ['name']}),
        ('Type ID',           {'fields': ['type_id']}),
    ]
    
admin.site.register(ELOType, ELOTypeAdmin)
admin.site.register(ReusabilityTreeNode, MPTTModelAdmin)