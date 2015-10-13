# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0004_elo_parent_elo'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='parent_elo_version',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='elo',
            name='version',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='elo',
            name='parent_elo',
            field=models.ForeignKey(default=0, blank=True, to='elos.ELO'),
        ),
    ]
