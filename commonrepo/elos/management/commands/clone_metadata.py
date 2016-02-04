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
Management command ``clone_metadata`` of ELOs in Common Repo projects.

This command will clone the metadata related with specefic ELOs.
'''

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from commonrepo.elos.models import ELO, ELOMetadata


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class Command(BaseCommand):
    help = 'Clone Metadata of ELOs'

    def add_arguments(self, parser):
        parser.add_argument('--source',
                            type=int,
                            help='Build Metadata of specific ELOs')
        parser.add_argument('--target',
                            nargs='+',
                            type=int,
                            help='Build Metadata of specific ELOs')

    def handle(self, *args, **options):
        try:
            elo_source = ELO.objects.get(id=options['source'])
        except ELO.DoesNotExist:
            raise CommandError(
                'Source ELO "%s" does not exist' %
                options['source'])

        if not elo_source.metadata:
            raise CommandError(
                'Source Metadata of ELO "%s" does not exist' %
                elo_source.id)

        for target in options['target']:
            try:
                elo_target = ELO.objects.get(id=target)
            except ELO.DoesNotExist:
                raise CommandError('ELO "%s" does not exist' % target)

            # Delete original metadata
            if elo_target.metadata:
                elo_target.metadata.delete()

            metadata = elo_source.metadata
            metadata.pk = None
            metadata.save()
            elo_target.metadata = metadata
            elo_target.save()

            self.stdout.write(
                'Successfully clone Metadata to target ELO "%s"' %
                elo_target.id)
