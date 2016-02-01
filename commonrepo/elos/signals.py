# -*- coding: utf-8 -*-

#
# Copyright 2016 edX PDR Lab, National Central University, Taiwan.
#
#     http://edxpdrlab.ncu.cc/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Created By: yrchen@ATCity.org
# Maintained By: yrchen@ATCity.org
#

from __future__ import absolute_import, unicode_literals

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
