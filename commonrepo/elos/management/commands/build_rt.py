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
Management command ``build_rt`` of ELOs in Common Repo projects.

This command will build the Reusabilliy Tree with specefic ELOs.
'''

from __future__ import absolute_import, unicode_literals

from django.core.management.base import BaseCommand, CommandError

from commonrepo.elos.models import ELO


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class Command(BaseCommand):
    help = 'Build RT of ELOs'

    def add_arguments(self, parser):
        parser.add_argument('--id',
                            nargs='+',
                            default=False,
                            type=int,
                            help='Build RT of specific ELOs')

        # Named (optional) arguments
        parser.add_argument('--all',
                            action='store_true',
                            dest='all',
                            default=False,
                            help='Build RT of all ELOs')

    def handle(self, *args, **options):
        if options['id']:
            self.stdout.write('Building RT of ELO "%s"...' % options['id'])
            for elo_id in options['id']:
                try:
                    elo = ELO.objects.get(pk=elo_id)
                except ELO.DoesNotExist:
                    raise CommandError('ELOs "%s" does not exist' % elo_id)

                elo.reusability_tree_build()

                self.stdout.write(
                    'Successfully builded RT of ELO "%s"' %
                    elo_id)

        if options['all']:
            elos = ELO.objects.all()

            self.stdout.write('Building RTs of all ELOs...')
            for elo in elos:
                elo.reusability_tree_build()
                self.stdout.write(
                    'Successfully builded RT of ELO "%s"' %
                    elo_id)

            self.stdout.write('Successfully builded RTs of all ELOs')
