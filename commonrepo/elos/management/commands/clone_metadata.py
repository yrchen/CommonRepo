# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from commonrepo.elos.models import ELO, ELOMetadata

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
            raise CommandError('Source ELO "%s" does not exist' % options['source'])

        if not elo_source.metadata:
            raise CommandError('Source Metadata of ELO "%s" does not exist' % elo_source.id)

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

            self.stdout.write('Successfully clone Metadata to target ELO "%s"' % elo_target.id)
