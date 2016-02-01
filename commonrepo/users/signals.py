# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db.models.signals import pre_delete, post_save

from actstream import action

from .models import User

# User has been registered with actstream.registry.register


def user_deleted_handler(sender, instance, **kwargs):
    action.send(instance, verb='was deleted')


def user_saved_handler(sender, instance, created, **kwargs):
    if created:
        action.send(instance, verb='was created')
    else:
        action.send(instance, verb='was updated')

pre_delete.connect(user_deleted_handler, sender=User)
post_save.connect(user_saved_handler, sender=User)
