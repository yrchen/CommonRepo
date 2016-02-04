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
Model configurations for Users in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from annoying.fields import AutoOneToOneField


@python_2_unicode_compatible
class User(AbstractUser):
    """
    Model for users in Common Repository project.
    """

    # First Name and Last Name do not cover name patterns
    # around the globe.

    # Basic User Information
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    organization = models.CharField(
        _("Organization/School"),
        blank=True,
        max_length=255)
    education = models.CharField(_("Education"), blank=True, max_length=255)
    url = models.URLField(_("URL"), blank=True)
    phone = models.CharField(_("Phone nubmer"), blank=True, max_length=255)
    address = models.CharField(_("Address"), blank=True, max_length=255)
    language = models.CharField(_("Language"), blank=True, max_length=255)
    area = models.CharField(_("Area/Nation"), blank=True, max_length=255)
    about = models.CharField(_("About Me"), blank=True, max_length=255)
    social_facebook = models.URLField(
        _("Social - Facebook"), blank=True, max_length=255)
    social_google = models.URLField(
        _("Social - Google Plus"),
        blank=True,
        max_length=255)
    social_linkedin = models.URLField(
        _("Social - Linkedin"), blank=True, max_length=255)
    social_twitter = models.URLField(
        _("Social - Twitter"), blank=True, max_length=255)

    # User Pedagogical Information
    teaching_category = models.CharField(
        _("Teaching Category"), blank=True, max_length=255)
    teaching_subject_area = models.CharField(
        _("Teaching Subject Area"), blank=True, max_length=255)

    # Preferences
    elo_similarity_threshold = models.FloatField(
        _("ELOs Similarity Threshold"), default=0)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


@python_2_unicode_compatible
class UserProfile(models.Model):
    """
    Model for user profile in Common Repository project.
    """

    from commonrepo.elos.models import ELO
    from commonrepo.groups.models import Group

    user = AutoOneToOneField(User, primary_key=True)
    friends = models.ManyToManyField(User, related_name='friend_with')
    follows = models.ManyToManyField(User, related_name='followed_by')
    follow_elos = models.ManyToManyField(ELO, related_name='followed_by')
    follow_groups = models.ManyToManyField(Group, related_name='followed_by')

    def __str__(self):
        return self.user.username
