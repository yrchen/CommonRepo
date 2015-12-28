# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig

from actstream import registry

class GroupsAppConfig(AppConfig):
    name = 'commonrepo.groups'

    def ready(self):
        registry.register(self.get_model('Group'))
        import commonrepo.groups.signals
