# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from commonrepo.elos.models import ELO, ELOMetadata

class Command(BaseCommand):
    help = 'Build Metadata of ELOs'

    def add_arguments(self, parser):
        parser.add_argument('--id',
                            nargs='+',
                            default=False,
                            type=int,
                            help='Build Metadata of specific ELOs')

        # Named (optional) arguments
        parser.add_argument('--all',
                            action='store_true',
                            dest='all',
                            default=False,
                            help='Build Metadata of all ELOs')

    def handle(self, *args, **options):
        if options['id']:
            for elo_id in options['id']:
                try:
                    elo = ELO.objects.get(pk=elo_id)
                except ELO.DoesNotExist:
                    raise CommandError('ELOs "%s" does not exist' % poll_id)

                if not elo.metadata:
                    metadata = ELOMetadata.objects.create()
                    elo.metadata = metadata
                    elo.save()

                self.stdout.write('Successfully builded Metadata of ELO "%s"' % poll_id)

        if options['all']:
            elos = ELO.objects.all()
            
            for elo in elos:
                if not elo.metadata:
                    metadata = ELOMetadata.objects.create()
                    elo.metadata = metadata
                    elo.save()

            self.stdout.write('Successfully builded Metadata of all ELOs')
