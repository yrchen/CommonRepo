# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0033_reusabilitytreenode_base_elo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reusabilitytreenode',
            name='elo_diversity',
            field=models.FloatField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='reusabilitytreenode',
            name='elo_similarity',
            field=models.FloatField(default=0, blank=True),
        ),
    ]
