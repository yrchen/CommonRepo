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
Form configurations for ELOs package in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.forms import ModelForm, ModelChoiceField
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from commonrepo.users.models import User as User

from .models import ELO, ELOMetadata


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class ELOMetadataUpdateForm(ModelForm):
    """
    Form of ELO Metadata update
    """

    class Meta:
        model = ELOMetadata
        fields = [
            #
            # 1. General

            # 1.1 identifier
            "General_identifier",
            # 1.2 title
            "General_title",
            # 1.3 language
            "General_language",
            # 1.4 description
            "General_description",
            # 1.5 keyword
            "General_keyword",
            # 1.6 coverage
            "General_coverage",
            # 1.7 structure
            "General_structure",
            # 1.8 aggregationLevel
            "General_aggregationLevel",

            #
            # 2. LifeCycle

            # 2.1 version
            "LifeCycle_version",
            # 2.2 status
            "LifeCycle_status",
            # 2.3 contribute
            "LifeCycle_contribute_role",
            "LifeCycle_contribute_entity",
            "LifeCycle_contribute_date_dateTime",
            "LifeCycle_contribute_date_description",

            #
            # 3. Meta-metadata

            # 3.1 Meta_metadata-identifier
            "Meta_metadata_identifier_catalog",
            "Meta_metadata_identifier_entry",
            # 3.2 Meta_metadata-contribute
            "Meta_metadata_contribute_role",
            "Meta_metadata_contribute_entity",
            "Meta_metadata_contribute_date_dateTime",
            "Meta_metadata_contribute_date_description",
            # 3.3 Meta_metadata-metadataSchema
            "Meta_metadata_metadataSchema",
            # 3.4 Meta_metadata-language
            "Meta_metadata_language",

            #
            # 4. Technical

            # 4.1 format
            "Technical_format",
            # 4.2 size
            "Technical_size",
            # 4.3 location
            "Technical_location",
            # 4.4 requirement
            "Technical_requirement_orComposite_type",
            "Technical_requirement_orComposite_name",
            "Technical_requirement_orComposite_minimumVersion",
            "Technical_requirement_orComposite_maximumVersion",
            # 4.5 installationRemarks
            "Technical_installationRemarks",
            # 4.6 otherPlatformRequirements
            "Technical_otherPlatformRequirements",
            # 4.7 duration
            "Technical_duration_duration",
            "Technical_duration_description",

            #
            # 5. Educational

            # 5.1 interactivityTyp
            "Educational_interactivityType",
            # 5.2 learningResourceType
            "Educational_learningResourceType",
            # 5.3 interactivityLevel
            "Educational_interactivityLevel",
            # 5.4 semanticDensity
            "Educational_semanticDensity",
            # 5.5 intendedEndUserRole
            "Educational_intendedEndUserRole",
            # 5.6 context
            "Educational_context",
            # 5.7 typicalAgeRange
            "Educational_typicalAgeRange",
            # 5.8 difficulty
            "Educational_difficulty",
            # 5.9 typicalLearningTime
            "Educational_typicalLearningTime_duration",
            "Educational_typicalLearningTime_description",
            # 5.10 description
            "Educational_description",
            # 5.11 language
            "Educational_language",

            #
            # 6. Rights

            # 6.1 cost
            "Rights_cost",
            # 6.2 copyrightAndOtherRestrictions
            "Rights_copyrightAndOtherRestrictions",
            # 6.3 description
            "Rights_description",

            #
            # 7. Relation

            # 7.1 Kind
            "Relation_kind",
            # 7.2 Resource
            "Relation_resource_identifier_catalog",
            "Relation_resource_identifier_entry",
            "Relation_resource_description",

            #
            # 8. Annotation

            # 8.1 entity
            "Annotation_entity",
            # 8.2 date
            "Annotation_date_dateTime",
            "Annotation_date_description",
            # 8.3 description
            "Annotation_description",

            #
            # 9. Classification

            # 9.1 purpose
            "Classification_purpose",
            # 9.2 taxonPath
            "Classification_taxonPath_source",
            # 9.2.2 Classification-taxonPath-taxon
            "Classification_taxonPath_taxon",
            "Classification_taxonPath_taxon_id",
            "Classification_taxonPath_taxon_entry",
            # 9.3 description
            "Classification_description",
            # 9.4 keyword
            "Classification_keyword", ]

    def __init__(self, pk=None, *args, **kwargs):
        super(ELOMetadataUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))


class ELOForm(ModelForm):
    """
    Form of ELO
    """

    class Meta:
        model = ELO
        fields = [
            'name',
            'author',
            'cover',
            'description',
            'original_type',
            'license',
            'init_file']

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(ELOForm, self).__init__(*args, **kwargs)

        # check if user is not staff
        if not self.request_user.is_staff:
            self.fields["author"].queryset = User.objects.filter(
                username=self.request_user)
            self.fields["author"].widget.attrs['readonly'] = True

        # author can't be empty
        self.fields["author"].empty_label = None

        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))


class ELOForkForm(ModelForm):
    """
    Form of ELO Fork
    """

    class Meta:
        model = ELO
        fields = [
            'name',
            'author',
            'description',
            'original_type',
            'license',
            'init_file',
            'version',
            'parent_elo',
            'parent_elo_uuid',
            'parent_elo_version']

    def __init__(self, pk=None, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(ELOForkForm, self).__init__(*args, **kwargs)

        elo_original = get_object_or_404(ELO, id=pk)
        elo_source = elo_original

        # If original ELO is not public
        if not elo_original.is_public:
            # and request.user is not author or staff, use Root ELO to replace
            if not self.request_user == elo_original.author and not self.request_user.is_staff:
                elo_source = get_object_or_404(ELO, id=settings.ELO_ROOT_ID)

        self.fields["name"].initial = elo_source.name + \
            " (forked from author " + elo_source.author.username + ")"
        self.fields["name"].widget.attrs['readonly'] = True
        self.fields["author"].queryset = User.objects.filter(
            username=self.request_user)
        self.fields["author"].empty_label = None
        self.fields["author"].widget.attrs['readonly'] = True
        self.fields["description"].initial = elo_source.description
        self.fields["description"].widget.attrs['readonly'] = True
        self.fields["original_type"].initial = elo_source.original_type
        self.fields["original_type"].widget.attrs['readonly'] = True
        self.fields["license"].initial = elo_source.license
        self.fields["license"].widget.attrs['readonly'] = True
        self.fields["init_file"].initial = elo_source.init_file
        self.fields["init_file"].widget.attrs['readonly'] = True
        self.fields["version"].initial = 1
        self.fields["version"].widget.attrs['readonly'] = True

        # If original ELO is not public
        if not elo_original.is_public:
            # author and staff still can fork
            if self.request_user == elo_original.author or self.request_user.is_staff:
                self.fields["parent_elo"].queryset = ELO.objects.filter(
                    id=elo_original.id)
                self.fields["parent_elo_uuid"].initial = elo_original.uuid
                self.fields[
                    "parent_elo_version"].initial = elo_original.version
            # others will force to use Root ELO
            else:
                self.fields["parent_elo"].queryset = ELO.objects.filter(
                    id=settings.ELO_ROOT_ID)
                self.fields["parent_elo_uuid"].initial = elo_source.uuid
                self.fields["parent_elo_version"].initial = elo_source.version
        else:
            self.fields["parent_elo"].queryset = ELO.objects.filter(
                id=elo_original.id)
            self.fields["parent_elo_uuid"].initial = elo_original.uuid
            self.fields["parent_elo_version"].initial = elo_original.version

        self.fields["parent_elo"].empty_label = None
        self.fields["parent_elo"].widget.attrs['readonly'] = True
        self.fields["parent_elo_uuid"].widget.attrs['readonly'] = True
        self.fields["parent_elo_version"].widget.attrs['readonly'] = True

        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))


class ELOUpdateForm(ModelForm):
    """
    Form of ELO update
    """

    class Meta:
        model = ELO
        fields = [
            'name',
            'cover',
            'description',
            'original_type',
            'license',
            'metadata',
            'is_public',
            'init_file']

    def __init__(self, pk=None, *args, **kwargs):
        super(ELOUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))
