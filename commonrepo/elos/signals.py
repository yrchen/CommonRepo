# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db.models.signals import pre_delete, post_save

from actstream import action

from .models import ELO

# ELO has been registered with actstream.registry.register


def elo_deleted_handler(sender, instance, **kwargs):
    action.send(instance, verb='was deleted')


def elo_saved_handler(sender, instance, created, **kwargs):
    if created:
        action.send(instance, verb='was created')
    else:
        action.send(instance, verb='was updated')

pre_delete.connect(elo_deleted_handler, sender=ELO)
post_save.connect(elo_saved_handler, sender=ELO)
