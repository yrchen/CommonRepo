# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.

    # Basic User Information
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    organization = models.CharField(_("Organization/School"), blank=True, max_length=255)
    education = models.CharField(_("Education"), blank=True, max_length=255)
    url = models.URLField(_("URL"), blank=True)
    phone = models.CharField(_("Phone nubmer"), blank=True, max_length=255)
    address = models.CharField(_("Address"), blank=True, max_length=255)
    language =  models.CharField(_("Language"), blank=True, max_length=255)
    area = models.CharField(_("Area/Nation"), blank=True, max_length=255)

    # User Pedagogical Information
    teaching_category = models.CharField(_("Teaching Category"), blank=True, max_length=255)
    teaching_subject_area = models.CharField(_("Teaching Subject Area"), blank=True, max_length=255)
    
    # Preferences
    elo_similarity_threshold = models.FloatField(_("ELOs Similarity Threshold"), default=0)

    # Social Information
    friends = models.ManyToManyField('self', related_name='friends_with')
    followers = models.ManyToManyField('self', related_name='follow_by')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
