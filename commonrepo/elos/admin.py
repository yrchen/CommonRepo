# -*- coding: utf-8 -*-

#
# Copyright 2016 edX PDR Lab, National Central University, Taiwan.
#
#     http://edxpdrlab.ncu.cc/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Created By: yrchen@ATCity.org
# Maintained By: yrchen@ATCity.org
#

"""
Admin site configurations for ELOs in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from reversion_compare.admin import CompareVersionAdmin

from .models import ELO, ELOType, ELOMetadata, ReusabilityTreeNode, ReusabilityTree


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class ELOAdmin(CompareVersionAdmin):
    """
    Admin menu of ELO
    """

    fieldsets = [
        ('ELO Info', {
            'fields': [
                'name',
                'fullname',
                'author',
                'description',
                'uuid',
                'is_public',
                'init_file'
                ]
            }),
        ('ELO Metadata', {
            'fields': [
                'original_type',
                'metadata',
                'license'
                ]
            }),
        ('ELO Version', {
            'fields': [
                'version',
                'parent_elo',
                'parent_elo_uuid',
                'parent_elo_version'
                ]
            }),
    ]

admin.site.register(ELO, ELOAdmin)


class ELOTypeAdmin(CompareVersionAdmin):
    """
    Admin menu of ELO Type
    """

    fieldsets = [
        ('Type Name', {
            'fields': [
                'name'
                ]
            }),
        ('Type ID', {
            'fields': [
                'type_id'
                ]
            }),
    ]

admin.site.register(ELOType, ELOTypeAdmin)


class ELOMetadataAdmin(CompareVersionAdmin):
    """
    Admin menu of ELO Metadata
    """

    fieldsets = [
        ('Gerneral', {
            'fields': [
                'General_identifier',
                'General_title',
                'General_language',
                'General_description',
                'General_keyword',
                'General_coverage',
                'General_structure',
                'General_aggregationLevel'
                ]
            }),
        ('LifeCycle', {
            'fields': [
                'LifeCycle_version',
                'LifeCycle_status',
                'LifeCycle_contribute_role',
                'LifeCycle_contribute_entity',
                'LifeCycle_contribute_date_dateTime',
                'LifeCycle_contribute_date_description'
                ]
            }),
        ('Meta-metadata', {
            'fields': [
                'Meta_metadata_identifier_catalog',
                'Meta_metadata_identifier_entry',
                'Meta_metadata_contribute_role',
                'Meta_metadata_contribute_entity',
                'Meta_metadata_contribute_date_dateTime',
                'Meta_metadata_contribute_date_description',
                'Meta_metadata_metadataSchema',
                'Meta_metadata_language'
                ]
            }),
        ('Technical', {
            'fields': [
                'Technical_format',
                'Technical_size',
                'Technical_location',
                'Technical_requirement_orComposite_type',
                'Technical_requirement_orComposite_name',
                'Technical_requirement_orComposite_minimumVersion',
                'Technical_requirement_orComposite_maximumVersion',
                'Technical_installationRemarks',
                'Technical_otherPlatformRequirements',
                'Technical_duration_duration',
                'Technical_duration_description'
                ]
            }),
        ('Educational', {
            'fields': [
                'Educational_interactivityType',
                'Educational_learningResourceType',
                'Educational_interactivityLevel',
                'Educational_semanticDensity',
                'Educational_intendedEndUserRole',
                'Educational_context',
                'Educational_typicalAgeRange',
                'Educational_difficulty',
                'Educational_typicalLearningTime_duration',
                'Educational_typicalLearningTime_description',
                'Educational_description',
                'Educational_language'
                ]
            }),
        ('Rights', {
            'fields': [
                'Rights_cost',
                'Rights_copyrightAndOtherRestrictions',
                'Rights_description'
                ]
            }),
        ('Relation', {
            'fields': [
                'Relation_kind',
                'Relation_resource_identifier_catalog',
                'Relation_resource_identifier_entry',
                'Relation_resource_description'
                ]
            }),
        ('Annotation', {
            'fields': [
                'Annotation_entity',
                'Annotation_date_dateTime',
                'Annotation_date_description',
                'Annotation_description'
                ]
            }),
        ('Classification', {
            'fields': [
                'Classification_purpose',
                'Classification_taxonPath_source',
                'Classification_taxonPath_taxon',
                'Classification_taxonPath_taxon_id',
                'Classification_taxonPath_taxon_entry',
                'Classification_description',
                'Classification_keyword']
            })
    ]

admin.site.register(ELOMetadata, ELOMetadataAdmin)


class ReusabilityTreeAdmin(admin.ModelAdmin):
    """
    Admin menu of Reusability Tree
    """

    fieldsets = [
        ('Reusability Tree Info', {
            'fields': [
                'name']
            }),
        ('ELO Info', {
            'fields': [
                'base_elo',
                'elo_similarity',
                'elo_diversity']
            }),
        ('Reusability Tree Node', {
            'fields': [
                'root_node']
            }),
    ]

admin.site.register(ReusabilityTree, ReusabilityTreeAdmin)

admin.site.register(ReusabilityTreeNode, MPTTModelAdmin)
