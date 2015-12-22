# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from commonrepo.elos.models import ELO

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
            for elo_id in options['id']:
                try:
                    elo = ELO.objects.get(pk=elo_id)
                except ELO.DoesNotExist:
                    raise CommandError('ELOs "%s" does not exist' % elo_id)

                elo.reusability_tree_build()

                self.stdout.write('Successfully builded RT of ELO "%s"' % elo_id)

        if options['all']:
            elos = ELO.objects.all()

            for elo in elos:
                elo.reusability_tree_build()

            self.stdout.write('Successfully builded RTs of all ELOs')
