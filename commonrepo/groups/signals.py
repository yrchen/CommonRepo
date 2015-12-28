# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db.models.signals import pre_delete, post_save

from actstream import action

from .models import Group

# Group has been registered with actstream.registry.register

def group_deleted_handler(sender, instance, **kwargs):
    action.send(instance, verb='was deleted')

def group_saved_handler(sender, instance, created, **kwargs):
    if created:
        action.send(instance, verb='was created')
    else:
        action.send(instance, verb='was updated')

pre_delete.connect(group_deleted_handler, sender=Group)
post_save.connect(group_saved_handler, sender=Group)
