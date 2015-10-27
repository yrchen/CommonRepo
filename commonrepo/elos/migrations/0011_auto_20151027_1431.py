# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0010_auto_20151021_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='parent_elo2',
            field=models.ForeignKey(related_name='elos_parent2', default=1, blank=True, to='elos.ELO'),
        ),
        migrations.AddField(
            model_name='elo',
            name='parent_elo2_uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Parent ELO2 UUID', blank=True),
        ),
        migrations.AddField(
            model_name='elo',
            name='parent_elo2_version',
            field=models.PositiveIntegerField(default=0, verbose_name='Parent ELO2 version', blank=True),
        ),
    ]
