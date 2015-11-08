# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from uuid import uuid4
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from commonrepo.users.models import User as User

@python_2_unicode_compatible
class Group(models.Model):
    # basic infor
    name = models.CharField(_("Name of Group"), blank=False, max_length=255)
    fullname = models.CharField(_("Full Name of Group"), blank=True, max_length=255)
    creator = models.ForeignKey(User, related_name='commonrepo_groups')
    members = models.ManyToManyField(User, related_name='commonrepo_groups_members')
    description = models.CharField(_("Description of Group"), blank=True, max_length=255)
    # metadata
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    is_public = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups:groups-detail', kwargs={'pk': self.pk})
