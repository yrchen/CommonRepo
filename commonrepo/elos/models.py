# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from uuid import uuid4
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from commonrepo.users.models import User as User

def get_random_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('elo-documents/', filename)

@python_2_unicode_compatible
class ELO(models.Model):
    name = models.CharField(_("Name of ELO"), blank=False, max_length=255)
    fullname = models.CharField(_("Full Name of ELO"), blank=True, max_length=255)
    author = models.ForeignKey(User, related_name='elos')
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    original_type = models.SmallIntegerField()
    init_file = models.FileField(blank=True, default='', upload_to=get_random_filename)
    parent_elo = models.ForeignKey('self', blank=True, default=0)
    version = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('elos:elos-detail', kwargs={'pk': self.pk})

class ELOType(models.Model):
    name = models.CharField(_("Name of ELO type"), blank=False, max_length=255)
    type_id = models.SmallIntegerField()
    
    def __str__(self):
        return self.name    