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
Model configurations for ELOs package in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from uuid import uuid4
import math
import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from annoying.fields import AutoOneToOneField
from licenses.models import License
from mptt import models as MPTTmodels

from commonrepo.users.models import User as User


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


def get_random_filename(instance, filename):
    """
    Construct random filename for ELOs documents.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('elo-documents/', filename)


def elos_get_random_filename(instance, filename):
    """
    Construct random filename for ELOs.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('elos/' + str(instance.id), filename)


def elos_get_cover_filename(instance, filename):
    """
    Construct random filename for cover file of ELOs.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('elos-covers/' + str(instance.id), filename)


@python_2_unicode_compatible
class ELOMetadata(models.Model):
    """
    Model of ELO Metadata
    """

    #
    # 1. General

    # 1.1 identifier
    General_identifier = models.CharField(
        _("General-identifier"), blank=True, max_length=255)
    # 1.2 title
    General_title = models.CharField(
        _("General-title"), blank=True, max_length=255)
    # 1.3 language
    General_language = models.CharField(
        _("General-language"), blank=True, max_length=255)
    # 1.4 description
    General_description = models.CharField(
        _("General-description"), blank=True, max_length=255)
    # 1.5 keyword
    General_keyword = models.CharField(
        _("General-keyword"), blank=True, max_length=255)
    # 1.6 coverage
    General_coverage = models.CharField(
        _("General-coverage"), blank=True, max_length=255)
    # 1.7 structure
    General_structure = models.CharField(
        _("General-structure"), blank=True, max_length=255)
    # 1.8 aggregationLevel
    General_aggregationLevel = models.CharField(
        _("General-aggregationLevel"), blank=True, max_length=255)

    #
    # 2. LifeCycle

    # 2.1 version
    LifeCycle_version = models.CharField(
        _("LifeCycle-version"), blank=True, max_length=255)
    # 2.2 status
    LifeCycle_status = models.CharField(
        _("LifeCycle-status"), blank=True, max_length=255)
    # 2.3 contribute
    LifeCycle_contribute_role = models.CharField(
        _("LifeCycle-contribute-role"), blank=True, max_length=255)
    LifeCycle_contribute_entity = models.CharField(
        _("LifeCycle-contribute-entity"), blank=True, max_length=255)
    LifeCycle_contribute_date_dateTime = models.CharField(
        _("LifeCycle-contribute-date-dateTime"), blank=True, max_length=255)
    LifeCycle_contribute_date_description = models.CharField(
        _("LifeCycle-contribute-date-description"), blank=True, max_length=255)

    #
    # 3. Meta-metadata

    # 3.1 Meta_metadata-identifier
    Meta_metadata_identifier_catalog = models.CharField(
        _("Meta_metadata-identifier-catalog"), blank=True, max_length=255)
    Meta_metadata_identifier_entry = models.CharField(
        _("Meta_metadata-identifier-entry"), blank=True, max_length=255)
    # 3.2 Meta_metadata-contribute
    Meta_metadata_contribute_role = models.CharField(
        _("Meta-metadata-contribute-role"), blank=True, max_length=255)
    Meta_metadata_contribute_entity = models.CharField(
        _("Meta-metadata-contribute-entity"), blank=True, max_length=255)
    Meta_metadata_contribute_date_dateTime = models.CharField(
        _("Meta-metadata-contribute-date-dateTime"), blank=True, max_length=255)
    Meta_metadata_contribute_date_description = models.CharField(
        _("Meta-metadata-contribute-date-description"), blank=True, max_length=255)
    # 3.3 Meta_metadata-metadataSchema
    Meta_metadata_metadataSchema = models.CharField(
        _("Meta-metadata-metadataSchema"), blank=True, max_length=255)
    # 3.4 Meta_metadata-language
    Meta_metadata_language = models.CharField(
        _("Meta-metadata-language"), blank=True, max_length=255)

    #
    # 4. Technical

    # 4.1 format
    Technical_format = models.CharField(
        _("Technical-format"), blank=True, max_length=255)
    # 4.2 size
    Technical_size = models.CharField(
        _("Technical-size"), blank=True, max_length=255)
    # 4.3 location
    Technical_location = models.CharField(
        _("Technical-location"), blank=True, max_length=255)
    # 4.4 requirement
    Technical_requirement_orComposite_type = models.CharField(
        _("Technical-requirement-orComposite-type"), blank=True, max_length=255)
    Technical_requirement_orComposite_name = models.CharField(
        _("Technical-requirement-orComposite-name"), blank=True, max_length=255)
    Technical_requirement_orComposite_minimumVersion = models.CharField(
        _("Technical-requirement-orComposite-minimumVersion"), blank=True, max_length=255)
    Technical_requirement_orComposite_maximumVersion = models.CharField(
        _("Technical-requirement-orComposite-maximumVersion"), blank=True, max_length=255)
    # 4.5 installationRemarks
    Technical_installationRemarks = models.CharField(
        _("Technical-installationRemarks"), blank=True, max_length=255)
    # 4.6 otherPlatformRequirements
    Technical_otherPlatformRequirements = models.CharField(
        _("Technical-otherPlatformRequirements"), blank=True, max_length=255)
    # 4.7 duration
    Technical_duration_duration = models.CharField(
        _("Technical-duration-duration"), blank=True, max_length=255)
    Technical_duration_description = models.CharField(
        _("Technical-duration-description"), blank=True, max_length=255)

    #
    # 5. Educational

    # 5.1 interactivityTyp
    Educational_interactivityType = models.CharField(
        _("Educational-interactivityType"), blank=True, max_length=255)
    # 5.2 learningResourceType
    Educational_learningResourceType = models.CharField(
        _("Educational-learningResourceType"), blank=True, max_length=255)
    # 5.3 interactivityLevel
    Educational_interactivityLevel = models.CharField(
        _("Educational-interactivityLevel"), blank=True, max_length=255)
    # 5.4 semanticDensity
    Educational_semanticDensity = models.CharField(
        _("Educational-semanticDensity"), blank=True, max_length=255)
    # 5.5 intendedEndUserRole
    Educational_intendedEndUserRole = models.CharField(
        _("Educational-intendedEndUserRole"), blank=True, max_length=255)
    # 5.6 context
    Educational_context = models.CharField(
        _("Educational-context"), blank=True, max_length=255)
    # 5.7 typicalAgeRange
    Educational_typicalAgeRange = models.CharField(
        _("Educational-typicalAgeRange"), blank=True, max_length=255)
    # 5.8 difficulty
    Educational_difficulty = models.CharField(
        _("Educational-difficulty"), blank=True, max_length=255)
    # 5.9 typicalLearningTime
    Educational_typicalLearningTime_duration = models.CharField(
        _("Educational-typicalLearningTime-duration"), blank=True, max_length=255)
    Educational_typicalLearningTime_description = models.CharField(
        _("Educational-typicalLearningTime-description"), blank=True, max_length=255)
    # 5.10 description
    Educational_description = models.CharField(
        _("Educational-description"), blank=True, max_length=255)
    # 5.11 language
    Educational_language = models.CharField(
        _("Educational-language"), blank=True, max_length=255)

    #
    # 6. Rights

    # 6.1 cost
    Rights_cost = models.CharField(
        _("Rights-cost"), blank=True, max_length=255)
    # 6.2 copyrightAndOtherRestrictions
    Rights_copyrightAndOtherRestrictions = models.CharField(
        _("Rights-copyrightAndOtherRestrictions"), blank=True, max_length=255)
    # 6.3 description
    Rights_description = models.CharField(
        _("Rights-description"), blank=True, max_length=255)

    #
    # 7. Relation

    # 7.1 Kind
    Relation_kind = models.CharField(
        _("Relation-kind"), blank=True, max_length=255)
    # 7.2 Resource
    Relation_resource_identifier_catalog = models.CharField(
        _("Relation-resource-identifier-catalog"), blank=True, max_length=255)
    Relation_resource_identifier_entry = models.CharField(
        _("Relation-resource-identifier-entry"), blank=True, max_length=255)
    Relation_resource_description = models.CharField(
        _("Relation-resource-description"), blank=True, max_length=255)

    #
    # 8. Annotation

    # 8.1 entity
    Annotation_entity = models.CharField(
        _("Annotation-entity"), blank=True, max_length=255)
    # 8.2 date
    Annotation_date_dateTime = models.CharField(
        _("Annotation-date_dateTime"), blank=True, max_length=255)
    Annotation_date_description = models.CharField(
        _("Annotation-date-description"), blank=True, max_length=255)
    # 8.3 description
    Annotation_description = models.CharField(
        _("Annotation-description"), blank=True, max_length=255)

    #
    # 9. Classification

    # 9.1 purpose
    Classification_purpose = models.CharField(
        _("Classification-purpose"), blank=True, max_length=255)
    # 9.2 taxonPath
    Classification_taxonPath_source = models.CharField(
        _("Classification-taxonPath-source"), blank=True, max_length=255)
    # 9.2.2 Classification-taxonPath-taxon
    Classification_taxonPath_taxon = models.CharField(
        _("Classification-taxonPath-taxon"), blank=True, max_length=255)
    Classification_taxonPath_taxon_id = models.CharField(
        _("Classification-taxonPath-taxon-id"), blank=True, max_length=255)
    Classification_taxonPath_taxon_entry = models.CharField(
        _("Classification-taxonPath-taxon-entry"), blank=True, max_length=255)
    # 9.3 description
    Classification_description = models.CharField(
        _("Classification-description"), blank=True, max_length=255)
    # 9.4 keyword
    Classification_keyword = models.CharField(
        _("Classification-keyword"), blank=True, max_length=255)

    def compare(self, obj):
        """
        Wrapper fuction of ELOs Metadata comparing function.

        Arguments:
            obj (ELO):
                Target ELO to compare.

        This wrapper function only needs one argument `obj` for target ELO. The other arguments for
        comparing function will be passed directly for consistency function calls.
        """
        fields_excluded = 'id', '_state', '_elo_cache'
        return self._compare(self, obj, fields_excluded)

    def _compare(self, obj_source, obj_target, fields_excluded):
        """
        ELOs Metadata comparing function.

        Arguments:
            obj_source (ELO):
                Source ELO to compare.
            obj_target (ELO):
                Traget ELO that will be compared with source ELO.
            fields_excluded (string):
                The fields list that will be excluded to been compared.

        Return value:
            Dictionary `source` and `target` that representing the result.
            When the obj_source and obj_target have the different attribute of specific field of Metadata,
            the field name and attribute will been add into the dictionay `source` and `target`.
        """
        dict_source, dict_target = obj_source.__dict__, obj_target.__dict__
        source, target = {}, {}
        # Check all fields of Metadata
        for field, attribute in dict_source.items():
            if field in fields_excluded:
                continue
            try:
                if attribute != dict_target[field]:
                    source.update({field: attribute})
                    target.update({field: dict_target[field]})
            except KeyError:
                source.update({field: attribute})

        return source, target

    def match(self, obj):
        """
        Wrapper fuction of ELOs Metadata matching function.

        Arguments:
            obj (ELO):
                Target ELO to compare.

        This wrapper function only needs one argument `obj` for target ELO. The other arguments for
        matching function will be passed directly for consistency function calls.
        """
        fields_all = self._meta.get_all_field_names()
        fields_included = fields_all
        fields_excluded = 'id', '_state', '_elo_cache'
        return self._match(self, obj, fields_included, fields_excluded)

    def _match(self, obj_source, obj_target, fields_included, fields_excluded):
        """
        ELOs Metadata matching function.

        Arguments:
            obj_source (ELO):
                Source ELO to compare.
            obj_target (ELO):
                Traget ELO that will be matched with source ELO.
            fields_included (string):
                The fields list that will be included to been matched.
            fields_excluded (string):
                The fields list that will be excluded to been matched.

        Return value:
            Interger `counter_total` and `counter_matched` that representing the result.
            The value of `counter_total` repsents the total fields that obj_source contains attribute.
            When the obj_source and obj_target have the same attribute of specific field of Metadata,
            the value of `counter_matched` will been increased.
        """
        dict_source, dict_target = obj_source.__dict__, obj_target.__dict__
        counter_total, counter_matched = 0, 0

        for field, attribute in dict_source.items():
            # Check fileds that need to match
            if field in fields_excluded or field not in fields_included:
                continue

            try:
                # check source object has value
                if bool(attribute):
                    counter_total += 1
                    if attribute == dict_target[field]:
                        counter_matched += 1

            except KeyError:
                pass

        return counter_total, counter_matched

    def match2(self, obj):
        """
        Wrapper fuction of ELOs Metadata matching function.

        TODO:
            Still under construction, it will replace match() in the future.

        Arguments:
            obj (ELO):
                Target ELO to compare.

        This wrapper function only needs one argument `obj` for target ELO. The other arguments for
        matching function will be passed directly for consistency function calls.
        """
        fields_included = self._meta.get_all_field_names()
        fields_excluded = 'id', '_state', '_elo_cache'
        return self._match2(self, obj, fields_included, fields_excluded)

    def _match2(
            self,
            obj_source,
            obj_target,
            fields_included,
            fields_excluded):
        """
        ELOs Metadata matching function.

        TODO:
            Still under construction, it will replace _match() in the future.
            This function use different methods to campare the Metadata.
            The spec of Metadata of ELOs v1 was based on SCORM. For some technical reasons, the most
            learning objects on the popular MOOCs platforms (e.g., Open edX and Course Builder) don't
            follow the same spec of Metadata. The first version of _match() function provides an easy
            implementation of matching function, but it should been modified to provides more
            meaningful result in the future.

        Arguments:
            obj_source (ELO):
                Source ELO to compare.
            obj_target (ELO):
                Traget ELO that will be matched with source ELO.
            fields_included (string):
                The fields list that will be included to been matched.
            fields_excluded (string):
                The fields list that will be excluded to been matched.

        Return value:
            Interger `counter_total` and `counter_matched` that representing the result.
            The value of `counter_total` repsents the total fields that obj_source contains attribute.
            When the obj_source and obj_target have the same attribute of specific field of Metadata,
            the value of `counter_matched` will been increased.
        """

        #
        # Precise criteria (mandatory)
        #
        # 1.2 Title, 2.1 Version, 3.4 Language, 4.5 Installation Remarks,
        # 4.6 Other Platform Requirements, 6.3 Description, 7.2.1.1 Catalog, 7.2.1.2 Entry,
        # 8.1 Entity, 8.3 Description, 9.2.1 Source, 9.2.2.1 Id,
        # 9.2.2.2 Entry, and 9.3 Description
        fields_precise_criteria = (
            'General_title',
            'LifeCycle_version',
            'Meta_metadata_language',
            'Technical_installationRemarks',
            'Technical_otherPlatformRequirements',
            'Rights_description',
            'Relation_resource_identifier_catalog',
            'Relation_resource_identifier_entry',
            'Annotation_entity',
            'Annotation_description',
            'Classification_taxonPath_source',
            'Classification_taxonPath_taxon_id',
            'Classification_taxonPath_taxon_entry',
            'Classification_description')

        #
        # Incremental criteria (rewritable)
        #
        # 1.3 Language, 1.4 Description, 1.5 Keyword, 1.6 Coverage,
        # 2.3.2 Entity, 3.2.2 Entity, 4.1 Format, 4.3 Location,
        # 5.10 Description, 5.11 Language, 7.2.2 Description, and 9.4 Keyword
        fields_incremental_criteria = (
            'General_language',
            'General_description',
            'General_keyword',
            'General_coverage',
            'LifeCycle_contribute_entity',
            'Meta_metadata_contribute_entity',
            'Technical_format',
            'Technical_location',
            'Educational_description',
            'Educational_language',
            'Relation_resource_description',
            'Classification_keyword')

        #
        # Precedence criteria (rewritable)
        #
        # 4.2 Size, 4.4.1.3 Minimum Version, 4.4.1.4 Maximum Version, and 5.7
        # Typical Age Range
        fields_precedence_criteria = (
            'Technical_size',
            'Technical_requirement_orComposite_minimumVersion',
            'Technical_requirement_orComposite_maximumVersion',
            'Educational_typicalAgeRange')

        #
        # Time/duration criteria (rewritable)
        #
        # 2.3.3 Date, 3.2.3 Date,
        # 4.7 Duration, 5.9 Typical Learning Time, and 8.2 Date
        fields_time_duration_criteria = (
            'LifeCycle_contribute_date_dateTime',
            'LifeCycle_contribute_date_description',
            'Meta_metadata_contribute_date_dateTime',
            'Meta_metadata_contribute_date_description',
            'Technical_duration_duration',
            'Educational_typicalLearningTime_duration',
            'Educational_typicalLearningTime_description',
            'Annotation_date_dateTime',
            'Annotation_date_description')

        #
        # Single-choice criteria (rewritable)
        #
        # 1.7 Structure, 1.8 Aggregation Level, 2.2 Status, 2.3.1 Role,
        # 3.2.1 Role, 4.4.1.1 Type, 4.4.1.2 Name, 5.1 Interactivity Type,
        # 5.3 Interactivity Level, 5.4 Semantic Density, 5.8 Difficulty, 6.1 Cost,
        # 6.2 Copyright and Other Restrictions, 7.1 Kind, and 9.1 Purpose
        fields_single_choise_criteria = (
            'General_structure',
            'General_aggregationLevel',
            'LifeCycle_status',
            'LifeCycle_contribute_role',
            'Meta_metadata_contribute_role',
            'Technical_requirement_orComposite_type',
            'Technical_requirement_orComposite_name',
            'Educational_interactivityType',
            'Educational_interactivityLevel',
            'Educational_semanticDensity',
            'Educational_difficulty',
            'Rights_cost',
            'Rights_copyrightAndOtherRestrictions',
            'Relation_kind',
            'Classification_purpose')

        #
        # Many-choice criteria (rewritable)
        #
        # 3.3 Metadata Schema, 5.2 Learning Resource Type, 5.5 Intended End
        # User Role, and 5.6 Context
        fields_many_choise_criteria = (
            'Meta_metadata_metadataSchema',
            'Educational_learningResourceType',
            'Educational_intendedEndUserRole',
            'Educational_context')

        # V1: precise / single-choice criteria
        # V2: incremental criteria
        # V3: precedence / time/duration criteria
        # V4: many-choice critera

        dict_source, dict_target = obj_source.__dict__, obj_target.__dict__
        counter_total, counter_matched = 0, 0

        for field, attribute in dict_source.items():
            if field in fields_excluded or field not in fields_included:
                continue

            try:
                # check source object has value
                if bool(attribute):
                    counter_total += 1

                    # V1: precise / single-choice criteria
                    if field in fields_precise_criteria or field in fields_single_choise_criteria:
                        if attribute == dict_target[field]:
                            counter_matched += 1

                    # V2: incremental criteria
                    # f(Mi, Mj)
                    elif field in fields_incremental_criteria:
                        if attribute == dict_target[field]:
                            counter_matched += 1

                    # V3: precedence / time/duration criteria
                    # compare(Mi, Mj)
                    elif field in fields_precedence_criteria or field in fields_time_duration_criteria:
                        if attribute == dict_target[field]:
                            counter_matched += 1

                    # V4: many-choice critera
                    # disjunction(Mi, Mj)
                    elif field in fields_many_choise_criteria:
                        if attribute == dict_target[field]:
                            counter_matched += 1

            except KeyError:
                pass

        return counter_total, counter_matched

    def __str__(self):
        if hasattr(self, 'elo'):
            return str(self.elo.id) + ' - ' + self.elo.name
        else:
            return 'Metadata No.' + str(self.id)


@python_2_unicode_compatible
class ELOType(models.Model):
    """
    Model of ELO Type
    """

    name = models.CharField(_("Name of ELO type"), blank=False, max_length=255)
    type_id = models.SmallIntegerField(_("ELO Type ID"), unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('elos:elotypes-detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class ELO(models.Model):
    """
    Model of ELO
    """

    # basic infor
    name = models.CharField(_("Name of ELO"), blank=False, max_length=255)
    fullname = models.CharField(
        _("Full Name of ELO"),
        blank=True,
        max_length=255)
    description = models.CharField(
        _("Description of ELO"),
        blank=True,
        max_length=255)
    author = models.ForeignKey(User, related_name='elos')
    uuid = models.UUIDField(_("UUID"), default=uuid4)
    cover = models.ImageField(
        _("Cover of ELO"),
        blank=True,
        upload_to=elos_get_cover_filename)

    # metadata
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    metadata = AutoOneToOneField(ELOMetadata, null=True)
    license = models.ForeignKey(
        License,
        related_name='elos',
        blank=True,
        null=True)
    original_type = models.ForeignKey(
        ELOType,
        to_field='type_id',
        related_name='elos',
        blank=True,
        null=True)
    is_public = models.SmallIntegerField(default=0)
    init_file = models.FileField(
        blank=True,
        default='',
        upload_to=elos_get_random_filename)

    # version control
    version = models.PositiveIntegerField(
        _("ELO version"), blank=True, default=0)
    parent_elo = models.ForeignKey('self', blank=True, default=1)
    parent_elo_uuid = models.UUIDField(
        _("Parent ELO UUID"), blank=True, default=uuid4)
    parent_elo_version = models.PositiveIntegerField(
        _("Parent ELO version"), blank=True, default=0)
    parent_elo2 = models.ForeignKey(
        'self',
        blank=True,
        default=1,
        related_name='elos_parent2')
    parent_elo2_uuid = models.UUIDField(
        _("Parent ELO2 UUID"), blank=True, default=uuid4)
    parent_elo2_version = models.PositiveIntegerField(
        _("Parent ELO2 version"), blank=True, default=0)

    def get_name(self):
        return "ELO: " + self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.get_name()

    def get_absolute_url(self):
        return reverse('elos:elos-detail', kwargs={'pk': self.pk})

    def similarity(
            self,
            obj_target,
            threshold=settings.ELO_SIMILARITY_THRESHOLD):
        """
        Wrapper fuction of ELOs similarity caculation function.

        Arguments:
            obj_target (ELO):
                The target ELO.
            threshold (float):
                The value of threshold that identify the meaningful result.

        This wrapper function only needs one argument `obj_target` for target ELO. The other arguments for
        caculation function will be passed directly for consistency function calls.
        """
        return self._similarity(self, obj_target, threshold)

    def similarity_reverse(
            self,
            obj_target,
            threshold=settings.ELO_SIMILARITY_THRESHOLD):
        """
        Wrapper fuction of ELOs reverse similarity caculation function.

        Arguments:
            obj_target (ELO):
                The target ELO.
            threshold (float):
                The value of threshold that identify the meaningful result.

        This wrapper function only needs one argument `obj_target` for target ELO. The other arguments for
        caculation function will be passed directly for consistency function calls.
        """
        return self._similarity(obj_target, self, threshold)

    # Similarity caculation fucntion
    def _similarity(self, obj_source, obj_target, threshold):
        """
        ELOs similarity caculation function.

        Arguments:
            obj_source (ELO):
                The source ELO to compare.
            obj_target (ELO):
                The target ELO that will be matched with the source ELO.
            threshold (float):
                The value of threshold that identify the meaningful result.

        Return value:
            Float value that representing the result.
        """
        # Pass itself
        if not obj_source == obj_target:
            # Check the metadata of ELO exists
            if obj_source.metadata and obj_target.metadata:
                counter_total, counter_matched = obj_source.metadata.match(
                    obj_target.metadata)

                if counter_total and counter_matched:
                    result = float(counter_matched) / float(counter_total)

                    if result >= threshold:
                        return result
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 1

    def diversity(
            self,
            obj_target,
            threshold=settings.ELO_SIMILARITY_THRESHOLD):
        """
        ELOs diversity caculation function.

        Arguments:
            obj_target (ELO):
                Traget ELO that will be matched with source ELO.
            threshold (float):
                The value of threshold that identify the meaningful result.
                Default value is the setting of ELO_SIMILARITY_THRESHOLD.

        Return value:
            Float value that representing the result.
        """
        result = 0.0

        # Pass itself, there is no meaning to caculate the diversity with itself.
        if not self == obj_target:
            if self.similarity(obj_target, threshold):
                result += math.log(1 /
                                   self.similarity(obj_target, threshold)) / 2

            if self.similarity_reverse(obj_target, threshold):
                result += math.log(1 /
                                   self.similarity_reverse(obj_target, threshold)) / 2

        return result

    def reusability_tree_find_root(self):
        """
        Wrapper fuction to retrieve the root of ELO's reusability tree.

        Arguments:
            None.

        The self of object will been passed as argument `elo_source` to
        `_reusability_tree_find_root`.
        """
        return self._reusability_tree_find_root(self)

    def _reusability_tree_find_root(self, elo_source):
        """
        Retrieving function of the root of ELO's reusability tree.

        Arguments:
            elo_source (ELO):
                The source ELO that will been retrieved.

        Return value:
            ``ELO`` object that representing the result.
        """
        # If the parent ELO of the target ELO is not the Root ELO, use recursive to retrieve
        # the upper level of relations.
        if elo_source.parent_elo.id != settings.ELO_ROOT_ID:
            return self._reusability_tree_find_root(elo_source.parent_elo)
        else:
            return elo_source

    def reusability_tree_get_elo_similarity(
            self,
            elo_source,
            elo_target,
            threshold=settings.ELO_SIMILARITY_THRESHOLD):
        """
        Return the similarity value of the specific source and target ELOs.

        Arguments:
            elo_source (ELO):
                The source ELO to compare.
            elo_target (ELO):
                The target ELO that will be matched with the source ELO.
            threshold (float):
                The value of threshold that identify the meaningful result.
                Default value is the setting of ELO_SIMILARITY_THRESHOLD.

        Return value:
            Float value that representing the result.
        """
        return self._similarity(elo_source, elo_target, threshold)

    def reusability_tree_get_elo_similarity_reverse(
            self,
            elo_source,
            elo_target,
            threshold=settings.ELO_SIMILARITY_THRESHOLD):
        """
        Return the reverse similarity value of the specific source and target ELOs.

        Arguments:
            elo_source (ELO):
                The source ELO to compare.
            elo_target (ELO):
                The target ELO that will be matched with the source ELO.
            threshold (float):
                The value of threshold that identify the meaningful result.
                Default value is the setting of ELO_SIMILARITY_THRESHOLD.

        Return value:
            Float value that representing the result.
        """
        return self._similarity(elo_target, elo_source, threshold)

    def reusability_tree_get_elo_diversity(
            self,
            elo_source,
            elo_target,
            threshold=settings.ELO_SIMILARITY_THRESHOLD):
        """
        Return the diversity value of the specific source and target ELOs.

        Arguments:
            elo_source (ELO):
                The source ELO to compare.
            elo_target (ELO):
                The target ELO that will be matched with the source ELO.
            threshold (float):
                The value of threshold that identify the meaningful result.
                Default value is the setting of ELO_SIMILARITY_THRESHOLD.

        Return value:
            Float value that representing the result.
        """
        result = 0.0

        # Pass itself, there is no meaning to caculate the diversity with itself.
        if not elo_source == elo_target:
            if self.reusability_tree_get_elo_similarity(
                    elo_source, elo_target, threshold):
                result += math.log(1 /
                                   self.similarity(elo_target, threshold)) / 2

            if self.reusability_tree_get_elo_similarity_reverse(
                    elo_source, elo_target, threshold):
                result += math.log(1 /
                                   self.similarity_reverse(elo_target, threshold)) / 2

        return result

    def reusability_tree_build(self):
        """
        Wrapper function of building the reusability tree of the ELO.

        Arguments:
            None.

        Return value:
            None.
        """
        # Don't build RT when meet ELO Root
        if self.id == settings.ELO_ROOT_ID:
            pass
        else:
            # Check if Reusability Tree already exist, delete it first
            if hasattr(self, 'reusability_tree'):
                # Delete all related reusability tree nodes accodring base_elo
                # information
                reusability_tree_nodes = ReusabilityTreeNode.objects.filter(
                    base_elo=self)
                for reusability_tree_node in reusability_tree_nodes:
                    reusability_tree_node.delete()

                # Delete reusability tree
                self.reusability_tree.delete()

            # Create the object of reusability tree and setup the relationship with
            # the base ELO.
            reusability_tree = ReusabilityTree.objects.create(
                name=str(self.id) + '. ' + self.name,
                base_elo=self,
                root_node=self._reusability_tree_build(
                    self.reusability_tree_find_root(),
                    self))

    def _reusability_tree_build(self, elo_source, elo_base, node_parent=None):
        """
        Build the reusability tree of the ELO.

        Arguments:
            elo_source (ELO):
                The source ELO to build the reusability tree.
            elo_base (ELO):
                The base ELO of the reusability tree.
            node_parent: (ReusabilityTreeNode):
                The parent node of reusability tree.
                Default value is None.

        Return value:
            `ReusabilityTreeNode` object that representing the result.
        """
        reusability_tree_node = ReusabilityTreeNode.objects.create(
            name=str(elo_source.id) + '. ' + elo_source.name,
            parent=node_parent,
            elo=elo_source,
            elo_similarity=self.reusability_tree_get_elo_similarity(
                elo_base,
                elo_source),
            elo_diversity=self.reusability_tree_get_elo_diversity(
                elo_base,
                elo_source),
            base_elo=elo_base)

        # Find child
        elo_childs = ELO.objects.filter(parent_elo=elo_source)

        for elo in elo_childs:
            self._reusability_tree_build(elo, elo_base, reusability_tree_node)

        return reusability_tree_node

    def reusability_tree_update(self):
        """
        Update the reusability tree of the ELO.

        Arguments:
            None.

        Return value:
            None.

        This function only works for object itself.
        """
        self.reusability_tree_build()

    def has_permission(self, request_user):
        """
        Check the request_user have permission to access the object.

        Arguments:
            request_user (User):
                The User object that representing the specific user.
        """
        # Staff always have permission the access
        if request_user.is_staff:
            return True
        # Only author can access his/her own private ELOs
        else:
            if self.is_public:
                return True
            else:
                return self.author == request_user


@python_2_unicode_compatible
class ReusabilityTreeNode(MPTTmodels.MPTTModel):
    """
    Model of ELO Reusability Tree Node
    """

    name = models.CharField(max_length=260,
                            unique=False)   # ELO.name's max_length=255
    parent = MPTTmodels.TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True)
    elo = models.ForeignKey(ELO, blank=True, default=1)
    elo_similarity = models.FloatField(blank=True, default=0)
    elo_diversity = models.FloatField(blank=True, default=0)
    base_elo = models.ForeignKey(
        ELO,
        blank=True,
        default=1,
        related_name='reusability_tree_node')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


@python_2_unicode_compatible
class ReusabilityTree(models.Model):
    """
    Model of ELO Reusability Tree
    """

    name = models.CharField(max_length=260,
                            unique=False)   # ELO.name's max_length=255
    base_elo = models.OneToOneField(
        ELO,
        blank=True,
        null=True,
        related_name='reusability_tree')
    root_node = models.ForeignKey(ReusabilityTreeNode, blank=True)

    def __str__(self):
        return self.name
