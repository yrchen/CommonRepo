# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig


class MainAppConfig(AppConfig):
    name = 'commonrepo.main'

    def ready(self):
        import commonrepo.main.signals
