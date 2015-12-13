# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0031_auto_20151210_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reusabilitytree',
            name='base_elo',
            field=models.OneToOneField(related_name='reusability_tree', null=True, blank=True, to='elos.ELO'),
        ),
    ]
