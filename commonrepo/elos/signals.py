# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db.models.signals import post_save

from actstream import action

from .models import ELO

# ELO has been registered with actstream.registry.register

def elo_saved_handler(sender, instance, created, **kwargs):
    action.send(instance, verb='was saved')

post_save.connect(elo_saved_handler, sender=ELO)
