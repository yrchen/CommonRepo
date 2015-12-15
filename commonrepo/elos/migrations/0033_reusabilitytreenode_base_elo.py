# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0032_auto_20151213_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='reusabilitytreenode',
            name='base_elo',
            field=models.ForeignKey(related_name='reusability_tree_node', default=1, blank=True, to='elos.ELO'),
        ),
    ]
