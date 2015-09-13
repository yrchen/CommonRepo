# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from commonrepo.users.models import User

class ELOFileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, to_field='id')
    datafile = models.FileField()