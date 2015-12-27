# -*- coding: utf-8 -*-
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
                raise CommandError('Target Metadata of ELOs "%s" does not exist' % elo_target.id)

            elo_target.metadata.delete()
            self.stdout.write('Successfully delete Metadata of target ELO "%s"' % elo_target.id)
