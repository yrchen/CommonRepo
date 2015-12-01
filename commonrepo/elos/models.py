# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from uuid import uuid4
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from mptt import models as MPTTmodels

from commonrepo.users.models import User as User

def get_random_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('elo-documents/', filename)

@python_2_unicode_compatible
class ELOMetadata(models.Model):
    #
    # 1. General

    # 1.1 identifier
    General_identifier = models.CharField(_("General-identifier"), blank=True, max_length=255)
    # 1.2 title
    General_title = models.CharField(_("General-title"), blank=True, max_length=255)
    # 1.3 language
    General_language = models.CharField(_("General-language"), blank=True, max_length=255)
    # 1.4 description
    General_description = models.CharField(_("General-description"), blank=True, max_length=255)
    # 1.5 keyword
    General_keyword = models.CharField(_("General-keyword"), blank=True, max_length=255)
    # 1.6 coverage
    General_coverage = models.CharField(_("General-coverage"), blank=True, max_length=255)
    # 1.7 structure
    General_structure = models.CharField(_("General-structure"), blank=True, max_length=255)
    # 1.8 aggregationLevel
    General_aggregationLevel = models.CharField(_("General-aggregationLevel"), blank=True, max_length=255)

    #
    # 2. LifeCycle
    
    # 2.1 version
    LifeCycle_version = models.CharField(_("LifeCycle-version"), blank=True, max_length=255)
    # 2.2 status
    LifeCycle_status = models.CharField(_("LifeCycle-status"), blank=True, max_length=255)
    # 2.3 contribute
    LifeCycle_contribute_role = models.CharField(_("LifeCycle-contribute-role"), blank=True, max_length=255)
    LifeCycle_contribute_entity = models.CharField(_("LifeCycle-contribute-entity"), blank=True, max_length=255)
    LifeCycle_contribute_date_dateTime = models.CharField(_("LifeCycle-contribute-date-dateTime"), blank=True, max_length=255)
    LifeCycle_contribute_date_description = models.CharField(_("LifeCycle-contribute-date-description"), blank=True, max_length=255)

    #
    # 3. Meta-metadata

    # 3.1 Meta_metadata-identifier
    Meta_metadata_identifier_catalog = models.CharField(_("Meta_metadata-identifier-catalog"), blank=True, max_length=255)
    Meta_metadata_identifier_entry = models.CharField(_("Meta_metadata-identifier-entry"), blank=True, max_length=255)    
    # 3.2 Meta_metadata-contribute
    Meta_metadata_contribute_role = models.CharField(_("Meta-metadata-contribute-role"), blank=True, max_length=255)
    Meta_metadata_contribute_entity = models.CharField(_("Meta-metadata-contribute-entity"), blank=True, max_length=255)
    Meta_metadata_contribute_date_dateTime = models.CharField(_("Meta-metadata-contribute-date-dateTime"), blank=True, max_length=255)
    Meta_metadata_contribute_date_description = models.CharField(_("Meta-metadata-contribute-date-description"), blank=True, max_length=255)
    # 3.3 Meta_metadata-metadataSchema
    Meta_metadata_metadataSchema = models.CharField(_("Meta-metadata-metadataSchema"), blank=True, max_length=255)
    # 3.4 Meta_metadata-language
    Meta_metadata_language = models.CharField(_("Meta-metadata-language"), blank=True, max_length=255)

    #
    # 4. Technical

    # 4.1 format
    Technical_format = models.CharField(_("Technical-format"), blank=True, max_length=255)
    # 4.2 size
    Technical_size = models.CharField(_("Technical-size"), blank=True, max_length=255)
    # 4.3 location
    Technical_location = models.CharField(_("Technical-location"), blank=True, max_length=255)
    # 4.4 requirement
    Technical_requirement_orComposite_type = models.CharField(_("Technical-requirement-orComposite-type"), blank=True, max_length=255)
    Technical_requirement_orComposite_name = models.CharField(_("Technical-requirement-orComposite-name"), blank=True, max_length=255)
    Technical_requirement_orComposite_minimumVersion = models.CharField(_("Technical-requirement-orComposite-minimumVersion"), blank=True, max_length=255)
    Technical_requirement_orComposite_maximumVersion = models.CharField(_("Technical-requirement-orComposite-maximumVersion"), blank=True, max_length=255)
    # 4.5 installationRemarks
    Technical_installationRemarks = models.CharField(_("Technical-installationRemarks"), blank=True, max_length=255)
    # 4.6 otherPlatformRequirements
    Technical_otherPlatformRequirements = models.CharField(_("Technical-otherPlatformRequirements"), blank=True, max_length=255)
    # 4.7 duration
    Technical_duration_duration = models.CharField(_("Technical-duration-duration"), blank=True, max_length=255)
    Technical_duration_description = models.CharField(_("Technical-duration-description"), blank=True, max_length=255)

    #
    # 5. Educational

    # 5.1 interactivityTyp
    Educational_interactivityType = models.CharField(_("Educational-interactivityType"), blank=True, max_length=255)
    # 5.2 learningResourceType
    Educational_learningResourceType = models.CharField(_("Educational-learningResourceType"), blank=True, max_length=255)
    # 5.3 interactivityLevel
    Educational_interactivityLevel = models.CharField(_("Educational-interactivityLevel"), blank=True, max_length=255)
    # 5.4 semanticDensity
    Educational_semanticDensity = models.CharField(_("Educational-semanticDensity"), blank=True, max_length=255)
    # 5.5 intendedEndUserRole
    Educational_intendedEndUserRole = models.CharField(_("Educational-intendedEndUserRole"), blank=True, max_length=255)
    # 5.6 context
    Educational_context = models.CharField(_("Educational-context"), blank=True, max_length=255)
    # 5.7 typicalAgeRange
    Educational_typicalAgeRange = models.CharField(_("Educational-typicalAgeRange"), blank=True, max_length=255)
    # 5.8 difficulty
    Educational_difficulty = models.CharField(_("Educational-difficulty"), blank=True, max_length=255)
    # 5.9 typicalLearningTime
    Educational_typicalLearningTime_duration = models.CharField(_("Educational-typicalLearningTime-duration"), blank=True, max_length=255)
    Educational_typicalLearningTime_description = models.CharField(_("Educational-typicalLearningTime-description"), blank=True, max_length=255)
    # 5.10 description
    Educational_description = models.CharField(_("Educational-description"), blank=True, max_length=255)
    # 5.11 language
    Educational_language = models.CharField(_("Educational-language"), blank=True, max_length=255)

    #
    # 6. Rights

    # 6.1 cost
    Rights_cost = models.CharField(_("Rights-cost"), blank=True, max_length=255)
    # 6.2 copyrightAndOtherRestrictions
    Rights_copyrightAndOtherRestrictions = models.CharField(_("Rights-copyrightAndOtherRestrictions"), blank=True, max_length=255)
    # 6.3 description
    Rights_description = models.CharField(_("Rights-description"), blank=True, max_length=255)

    #
    # 7. Relation

    # 7.1 Kind
    Relation_kind = models.CharField(_("Relation-kind"), blank=True, max_length=255)
    # 7.2 Resource
    Relation_resource_identifier_catalog = models.CharField(_("Relation-resource-identifier-catalog"), blank=True, max_length=255)
    Relation_resource_identifier_entry = models.CharField(_("Relation-resource-identifier-entry"), blank=True, max_length=255)
    Relation_resource_description = models.CharField(_("Relation-resource-description"), blank=True, max_length=255)

    #
    # 8. Annotation

    # 8.1 entity
    Annotation_entity = models.CharField(_("Annotation-entity"), blank=True, max_length=255)
    # 8.2 date
    Annotation_date_dateTime = models.CharField(_("Annotation-date_dateTime"), blank=True, max_length=255)
    Annotation_date_description = models.CharField(_("Annotation-date-description"), blank=True, max_length=255)    
    # 8.3 description
    Annotation_description = models.CharField(_("Annotation-description"), blank=True, max_length=255)

    #
    # 9. Classification

    # 9.1 purpose
    Classification_purpose = models.CharField(_("Classification-purpose"), blank=True, max_length=255)
    # 9.2 taxonPath
    Classification_taxonPath_source = models.CharField(_("Classification-taxonPath-source"), blank=True, max_length=255)
    # 9.2.2 Classification-taxonPath-taxon
    Classification_taxonPath_taxon = models.CharField(_("Classification-taxonPath-taxon"), blank=True, max_length=255)
    Classification_taxonPath_taxon_id = models.CharField(_("Classification-taxonPath-taxon-id"), blank=True, max_length=255)
    Classification_taxonPath_taxon_entry = models.CharField(_("Classification-taxonPath-taxon-entry"), blank=True, max_length=255)
    # 9.3 description
    Classification_description = models.CharField(_("Classification-description"), blank=True, max_length=255)
    # 9.4 keyword
    Classification_keyword = models.CharField(_("Classification-keyword"), blank=True, max_length=255)
    
    def compare(self, obj):
        excluded_keys = 'id', '_state'
        return self._compare(self, obj, excluded_keys)
    
    def _compare(self, obj1, obj2, excluded_keys):
        d1, d2 = obj1.__dict__, obj2.__dict__
        old, new = {}, {}
        for k,v in d1.items():
            if k in excluded_keys:
                continue
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})

        return old, new

    def match(self, obj):
        #
        # Precise criteria (mandatory)
        #
        # 1.2 Title, 2.1 Version, 3.4 Language, 4.5 Installation Remarks,
        # 4.6 Other Platform Requirements, 6.3 Description, 7.2.1.1 Catalog, 7.2.1.2 Entry,
        # 8.1 Entity, 8.3 Description, 9.2.1 Source, 9.2.2.1 Id,
        # 9.2.2.2 Entry, and 9.3 Description
        keys_precise_criteria = ('General_title', 'LifeCycle_version', 'Meta_metadata_language', 'Technical_installationRemarks',
                                 'Technical_otherPlatformRequirements', 'Rights_description', 'Relation_resource_identifier_catalog', 'Relation_resource_identifier_entry',
                                 'Annotation_entity', 'Annotation_description', 'Classification_taxonPath_source', 'Classification_taxonPath_taxon_id',
                                 'Classification_taxonPath_taxon_entry', 'Classification_description')

        #
        # Incremental criteria (rewritable)
        #
        # 1.3 Language, 1.4 Description, 1.5 Keyword, 1.6 Coverage,
        # 2.3.2 Entity, 3.2.2 Entity, 4.1 Format, 4.3 Location,
        # 5.10 Description, 5.11 Language, 7.2.2 Description, and 9.4 Keyword
        keys_incremental_criteria = ('General_language', 'General_description', 'General_keyword', 'General_coverage',
                                     'LifeCycle_contribute_entity', 'Meta_metadata_contribute_entity', 'Technical_format', 'Technical_location',
                                     'Educational_description', 'Educational_language', 'Relation_resource_description', 'Classification_keyword')

        #
        # Precedence criteria (rewritable)
        #
        # 4.2 Size, 4.4.1.3 Minimum Version, 4.4.1.4 Maximum Version, and 5.7 Typical Age Range
        keys_precedence_criteria = ('Technical_size', 'Technical_requirement_orComposite_minimumVersion', 'Technical_requirement_orComposite_maximumVersion', 'Educational_typicalAgeRange')

        #
        # Time/duration criteria (rewritable)
        #
        # 2.3.3 Date, 3.2.3 Date, 
        # 4.7 Duration, 5.9 Typical Learning Time, and 8.2 Date
        keys_time_duration_criteria = ('LifeCycle_contribute_date_dateTime', 'LifeCycle_contribute_date_description', 'Meta_metadata_contribute_date_dateTime', 'Meta_metadata_contribute_date_description',
                                       'Technical_duration_duration', 'Educational_typicalLearningTime_duration', 'Educational_typicalLearningTime_description', 'Annotation_date_dateTime', 'Annotation_date_description')

        #
        # Single-choice criteria (rewritable)
        #
        # 1.7 Structure, 1.8 Aggregation Level, 2.2 Status, 2.3.1 Role,
        # 3.2.1 Role, 4.4.1.1 Type, 4.4.1.2 Name, 5.1 Interactivity Type,
        # 5.3 Interactivity Level, 5.4 Semantic Density, 5.8 Difficulty, 6.1 Cost,
        # 6.2 Copyright and Other Restrictions, 7.1 Kind, and 9.1 Purpose
        keys_single_choise_criteria = ('General_structure', 'General_aggregationLevel', 'LifeCycle_status', 'LifeCycle_contribute_role',
                                       'Meta_metadata_contribute_role', 'Technical_requirement_orComposite_type', 'Technical_requirement_orComposite_name', 'Educational_interactivityType',
                                       'Educational_interactivityLevel', 'Educational_semanticDensity', 'Educational_difficulty', 'Rights_cost',
                                       'Rights_copyrightAndOtherRestrictions', 'Relation_kind', 'Classification_purpose')

        #
        # Many-choice criteria (rewritable)
        #
        # 3.3 Metadata Schema, 5.2 Learning Resource Type, 5.5 Intended End User Role, and 5.6 Context
        keys_many_choise_criteria = ('Meta_metadata_metadataSchema', 'Educational_learningResourceType', 'Educational_intendedEndUserRole', 'Educational_context')

        # V1: precise / single-choice criteria
        # V2: incremental criteria
        # V3: precedence / time/duration criteria
        # V4: many-choice critera
        included_keys = ''
        excluded_keys = 'id', '_state'
        return self._match(self, obj, included_keys, excluded_keys)

    def _match(self, obj1, obj2, included_keys, excluded_keys):
        d1, d2 = obj1.__dict__, obj2.__dict__
        old, new = {}, {}

        for k,v in d1.items():
            if k in excluded_keys or k not in included_keys:
                continue
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})

        return old, new

    def __str__(self):
            return str(self.elo.id) + ' - ' + self.elo.name

@python_2_unicode_compatible
class ELOType(models.Model):
    name = models.CharField(_("Name of ELO type"), blank=False, max_length=255)
    type_id = models.SmallIntegerField(_("ELO Type ID"), unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('elos:elotypes-detail', kwargs={'pk': self.pk})

@python_2_unicode_compatible
class ELO(models.Model):
    # basic infor
    name = models.CharField(_("Name of ELO"), blank=False, max_length=255)
    fullname = models.CharField(_("Full Name of ELO"), blank=True, max_length=255)
    author = models.ForeignKey(User, related_name='elos')
    uuid = models.UUIDField(_("UUID"), default=uuid4)
    # metadata
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    metadata = models.OneToOneField(ELOMetadata, blank=True, null=True)
    original_type = models.ForeignKey(ELOType, to_field='type_id', related_name='elos')
    is_public = models.SmallIntegerField(default=0)
    init_file = models.FileField(blank=True, default='', upload_to=get_random_filename)
    # version control
    version = models.PositiveIntegerField(_("ELO version"), blank=True, default=0)
    parent_elo = models.ForeignKey('self', blank=True, default=1)
    parent_elo_uuid = models.UUIDField(_("Parent ELO UUID"), blank=True, default=uuid4)
    parent_elo_version = models.PositiveIntegerField(_("Parent ELO version"), blank=True, default=0)
    parent_elo2 = models.ForeignKey('self', blank=True, default=1, related_name='elos_parent2')
    parent_elo2_uuid = models.UUIDField(_("Parent ELO2 UUID"), blank=True, default=uuid4)
    parent_elo2_version = models.PositiveIntegerField(_("Parent ELO2 version"), blank=True, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('elos:elos-detail', kwargs={'pk': self.pk})

@python_2_unicode_compatible
class ReusabilityTreeNode(MPTTmodels.MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = MPTTmodels.TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    elo = models.ForeignKey(ELO, blank=True, default=1)
    
    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

@python_2_unicode_compatible
class ReusabilityTree(models.Model):
    name = models.CharField(max_length=50, unique=True)
    base_elo = models.ForeignKey(ELO, blank=True, default=1, related_name='reusability_tree')
    root_node = models.ForeignKey(ReusabilityTreeNode, blank=True)
    
    def __str__(self):
        return self.name
