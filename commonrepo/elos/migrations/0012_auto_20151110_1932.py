# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0011_auto_20151027_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='original_type',
            field=models.ForeignKey(related_name='elos', to='elos.ELOType', to_field='type_id'),
        ),
        migrations.AlterField(
            model_name='elotype',
            name='type_id',
            field=models.SmallIntegerField(unique=True),
        ),
    ]
