# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig
from actstream import registry

class ELOsAppConfig(AppConfig):
    name = 'commonrepo.elos'

    def ready(self):
        registry.register(self.get_model('ELO'))
