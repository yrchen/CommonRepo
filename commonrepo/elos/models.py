# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from uuid import uuid4
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

from commonrepo.users.models import User as User

def get_random_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('elo-documents/', filename)

@python_2_unicode_compatible
class ReusabilityTreeNode(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return self.name    

    class MPTTMeta:
        order_insertion_by = ['name']    

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
