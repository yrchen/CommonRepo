# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from commonrepo.users.models import User as User

@python_2_unicode_compatible
class ELO(models.Model):
    name = models.CharField(_("Name of ELO"), blank=False, max_length=255)
    fullname = models.CharField(_("Full Name of ELO"), blank=True, max_length=255)
    author = models.ForeignKey(User, related_name='elos')
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    original_type = models.SmallIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('elos:elos-view', kwargs={'pk': self.pk})

class ELOType(models.Model):
    name = models.CharField(_("Name of ELO type"), blank=False, max_length=255)
    type_id = models.SmallIntegerField()
    
    def __str__(self):
        return self.name    