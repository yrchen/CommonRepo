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

class ELOMetadata(models.Model):
    # General
    General_identifier = models.CharField(_("General-identifier"), blank=True, max_length=255)
    General_title = models.CharField(_("General-title"), blank=True, max_length=255)
    General_language = models.CharField(_("General-language"), blank=True, max_length=255)
    General_description = models.CharField(_("General-description"), blank=True, max_length=255)
    General_keyword = models.CharField(_("General-keyword"), blank=True, max_length=255)
    General_coverage = models.CharField(_("General-coverage"), blank=True, max_length=255)
    General_structure = models.CharField(_("General-structure"), blank=True, max_length=255)
    General_aggregationLevel = models.CharField(_("General-aggregationLevel"), blank=True, max_length=255)
    # LifeCycle
    LifeCycle_version = models.CharField(_("LifeCycle-version"), blank=True, max_length=255)
    LifeCycle_status = models.CharField(_("LifeCycle-status"), blank=True, max_length=255)
    LifeCycle_contribute = models.CharField(_("LifeCycle-contribute"), blank=True, max_length=255)
    # Meta-metadata
    Meta_metadata_identifier = models.CharField(_("Meta-metadata-identifier"), blank=True, max_length=255)
    Meta_metadata_contribute = models.CharField(_("Meta-metadata-contribute"), blank=True, max_length=255)
    Meta_metadata_metadataSchema = models.CharField(_("Meta-metadata-metadataSchema"), blank=True, max_length=255)
    Meta_metadata_language = models.CharField(_("Meta-metadata-language"), blank=True, max_length=255)
    # Technical
    Technical_format = models.CharField(_("Technical-format"), blank=True, max_length=255)
    Technical_size = models.CharField(_("Technical-size"), blank=True, max_length=255)
    Technical_location = models.CharField(_("Technical-location"), blank=True, max_length=255)
    Technical_requirement = models.CharField(_("Technical-requirement"), blank=True, max_length=255)
    Technical_installationRemarks = models.CharField(_("Technical-installationRemarks"), blank=True, max_length=255)
    Technical_otherPlatformRequirements = models.CharField(_("Technical-otherPlatformRequirements"), blank=True, max_length=255)
    Technical_duration = models.CharField(_("Technical-duration"), blank=True, max_length=255)
    # Educational
    Educational_interactivityType = models.CharField(_("Educational-interactivityType"), blank=True, max_length=255)
    Educational_learningResourceType = models.CharField(_("Educational-learningResourceType"), blank=True, max_length=255)
    Educational_interactivityLevel = models.CharField(_("Educational-interactivityLevel"), blank=True, max_length=255)
    Educational_semanticDensity = models.CharField(_("Educational-semanticDensity"), blank=True, max_length=255)
    Educational_intendedEndUserRole = models.CharField(_("Educational-intendedEndUserRole"), blank=True, max_length=255)
    Educational_context = models.CharField(_("Educational-context"), blank=True, max_length=255)
    Educational_typicalAgeRange = models.CharField(_("Educational-typicalAgeRange"), blank=True, max_length=255)
    Educational_difficulty = models.CharField(_("Educational-difficulty"), blank=True, max_length=255)
    Educational_typicalLearningTime = models.CharField(_("Educational-typicalLearningTime"), blank=True, max_length=255)
    Educational_description = models.CharField(_("Educational-description"), blank=True, max_length=255)
    Educational_language = models.CharField(_("Educational-language"), blank=True, max_length=255)
    # Rights
    Rights_cost = models.CharField(_("Rights-cost"), blank=True, max_length=255)
    Rights_copyrightAndOtherRestrictions = models.CharField(_("Rights-copyrightAndOtherRestrictions"), blank=True, max_length=255)
    Rights_description = models.CharField(_("Rights-description"), blank=True, max_length=255)
    # Relation
    Relation_kind = models.CharField(_("Relation-kind"), blank=True, max_length=255)
    Relation_resource = models.CharField(_("Relation-resource"), blank=True, max_length=255)
    # Annotation
    Annotation_entity = models.CharField(_("Annotation-entity"), blank=True, max_length=255)
    Annotation_date = models.CharField(_("Annotation-date"), blank=True, max_length=255)
    Annotation_description = models.CharField(_("Annotation-description"), blank=True, max_length=255)
    # Classification
    Classification_purpose = models.CharField(_("Classification-purpose"), blank=True, max_length=255)
    Classification_taxonPath = models.CharField(_("Classification-taxonPath"), blank=True, max_length=255)
    Classification_description = models.CharField(_("Classification-description"), blank=True, max_length=255)
    Classification_keyword = models.CharField(_("Classification-keyword"), blank=True, max_length=255)

@python_2_unicode_compatible
class ELOType(models.Model):
    name = models.CharField(_("Name of ELO type"), blank=False, max_length=255)
    type_id = models.SmallIntegerField(_("ELO Type ID"), unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('elos:elotypes-detail', kwargs={'pk': self.pk})
    

class ELO(models.Model):
    # basic infor
    name = models.CharField(_("Name of ELO"), blank=False, max_length=255)
    fullname = models.CharField(_("Full Name of ELO"), blank=True, max_length=255)
    author = models.ForeignKey(User, related_name='elos')
    uuid = models.UUIDField(_("UUID"), default=uuid4)
    # metadata
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
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

class ReusabilityTreeNode(MPTTmodels.MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = MPTTmodels.TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    elo = models.ForeignKey(ELO, blank=True, default=1)
    
    def __str__(self):
        return self.name    

    class MPTTMeta:
        order_insertion_by = ['name']    

class ReusabilityTree(models.Model):
    name = models.CharField(max_length=50, unique=True)
    base_elo = models.ForeignKey(ELO, blank=True, default=1, related_name='reusability_tree')
    root_node = models.ForeignKey(ReusabilityTreeNode, blank=True)
    
    def __str__(self):
        return self.name    
