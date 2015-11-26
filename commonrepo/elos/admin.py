# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import ELO, ELOType, ELOMetadata, ReusabilityTreeNode, ReusabilityTree

class ELOAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ELO Info',         {'fields': ['name', 'fullname', 'author', 'uuid']}),
        ('ELO Metadata',     {'fields': ['original_type', 'metadata']}),
        ('ELO Version',      {'fields': ['version', 'parent_elo', 'parent_elo_uuid', 'parent_elo_version']}),
    ]
    
admin.site.register(ELO, ELOAdmin)

class ELOTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Type Name',         {'fields': ['name']}),
        ('Type ID',           {'fields': ['type_id']}),
    ]
    
admin.site.register(ELOType, ELOTypeAdmin)

class ELOMetadataAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Gerneral', {
                'fields': ['General_identifier', 'General_title', 
                           'General_language', 'General_description', 
                           'General_keyword', 'General_coverage', 
                           'General_structure', 'General_aggregationLevel']
            }
        ),
        (
            'LifeCycle', {
                'fields': ['LifeCycle_version', 'LifeCycle_status', 
                           'LifeCycle_contribute']
            }
        ),
        (
            'Meta-metadata', {
                'fields': ['Meta_metadata_identifier', 'Meta_metadata_contribute', 
                           'Meta_metadata_metadataSchema', 'Meta_metadata_language']
            },
        ),
        (
            'Technical', {
                'fields': ['Technical_format', 'Technical_size', 
                           'Technical_location', 'Technical_requirement', 
                           'Technical_installationRemarks', 'Technical_otherPlatformRequirements',
                           'Technical_duration']
            },
        ),
        (
            'Educational', {
                'fields': ['Educational_interactivityType', 'Educational_learningResourceType',
                           'Educational_interactivityLevel', 'Educational_semanticDensity',
                           'Educational_intendedEndUserRole', 'Educational_context',
                           'Educational_typicalAgeRange', 'Educational_difficulty',
                           'Educational_typicalLearningTime', 'Educational_description',
                           'Educational_language']
            },
        ),
        (
            'Rights', {
                'fields': ['Rights_cost', 'Rights_copyrightAndOtherRestrictions',
                           'Rights_description']
            },
        ),
        (
            'Relation', {
                'fields': ['Relation_kind', 'Relation_resource']
            },
        ),
        (
            'Annotation', {
                'fields': ['Annotation_entity', 'Annotation_date',
                           'Annotation_description']
            },
        ),
        (
            'Classification', {
                'fields': ['Classification_purpose', 'Classification_taxonPath',
                           'Classification_description', 'Classification_keyword']
            },
        ),
    ]

admin.site.register(ELOMetadata, ELOMetadataAdmin)

admin.site.register(ReusabilityTreeNode, MPTTModelAdmin)

class ReusabilityTreeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Reusability Tree Info',         {'fields': ['name']}),
        ('ELO Info',                      {'fields': ['base_elo']}),
        ('Reusability Tree Node',         {'fields': ['root_node']}),
    ]

admin.site.register(ReusabilityTree, ReusabilityTreeAdmin)