# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0003_auto_20151012_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='parent_elo',
            field=models.ForeignKey(default=0, blank=True, to='elos.ELO'),
        ),
    ]
