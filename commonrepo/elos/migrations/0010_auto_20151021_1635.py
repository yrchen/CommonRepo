# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0009_elo_parent_elo_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='parent_elo_uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Parent ELO UUID', blank=True),
        ),
        migrations.AlterField(
            model_name='elo',
            name='parent_elo_version',
            field=models.PositiveIntegerField(default=0, verbose_name='Parent ELO version', blank=True),
        ),
        migrations.AlterField(
            model_name='elo',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='elo',
            name='version',
            field=models.PositiveIntegerField(default=0, verbose_name='ELO version', blank=True),
        ),
    ]
