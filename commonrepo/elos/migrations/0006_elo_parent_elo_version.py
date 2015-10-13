# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0005_elo_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='parent_elo_version',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
    ]
