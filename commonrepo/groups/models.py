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
Model configurations for Groups in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from uuid import uuid4
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from commonrepo.users.models import User as User


def groups_get_random_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('groups/' + str(instance.id), filename)


@python_2_unicode_compatible
class Group(models.Model):
    # basic infor
    name = models.CharField(_("Name of Group"), blank=False, max_length=255)
    fullname = models.CharField(
        _("Full Name of Group"),
        blank=True,
        max_length=255)
    creator = models.ForeignKey(User, related_name='commonrepo_groups')
    members = models.ManyToManyField(
        User, blank=True, related_name='commonrepo_groups_members')
    description = models.CharField(
        _("Description of Group"),
        blank=True,
        max_length=255)
    logo = models.ImageField(
        _("Logo of Group"),
        blank=True,
        upload_to=groups_get_random_filename)

    # metadata
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    is_public = models.SmallIntegerField(default=0)

    def get_name(self):
        return "Group: " + self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.get_name()

    def get_absolute_url(self):
        return reverse('groups:groups-detail', kwargs={'pk': self.pk})
