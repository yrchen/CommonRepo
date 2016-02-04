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

'''
Management command ``delete_metadata`` of ELOs in Common Repo projects.

This command will delete the metadata related with specefic ELOs.
'''

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from commonrepo.elos.models import ELO, ELOMetadata


class Command(BaseCommand):
    help = 'Delete Metadata of ELOs'

    def add_arguments(self, parser):
        parser.add_argument('--target',
                            nargs='+',
                            type=int,
                            help='Delete Metadata of specific ELOs')

    def handle(self, *args, **options):
        for target in options['target']:
            try:
                elo_target = ELO.objects.get(id=target)
            except ELO.DoesNotExist:
                raise CommandError('Target ELO "%s" does not exist' % target)

            if not elo_target.metadata:
                raise CommandError(
                    'Target Metadata of ELOs "%s" does not exist' %
                    elo_target.id)

            elo_target.metadata.delete()
            self.stdout.write(
                'Successfully delete Metadata of target ELO "%s"' %
                elo_target.id)
