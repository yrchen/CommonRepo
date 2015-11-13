# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0015_auto_20151113_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='reusabilitytreenode',
            name='elo',
            field=models.ForeignKey(default=1, blank=True, to='elos.ELO'),
        ),
    ]
