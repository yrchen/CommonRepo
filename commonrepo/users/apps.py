# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig

from actstream import registry


class UsersAppConfig(AppConfig):
    name = 'commonrepo.users'

    def ready(self):
        registry.register(self.get_model('User'))
        import commonrepo.users.signals
