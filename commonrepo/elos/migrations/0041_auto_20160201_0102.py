# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0040_elo_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='original_type',
            field=models.ForeignKey(related_name='elos', to_field='type_id', blank=True, to='elos.ELOType', null=True),
        ),
    ]
