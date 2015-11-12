# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0016_reusabilitytreenode_elo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReusabilityTree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('base_elo', models.ForeignKey(related_name='reusability_tree', default=1, blank=True, to='elos.ELO')),
                ('root_node', models.ForeignKey(to='elos.ReusabilityTreeNode', blank=True)),
            ],
        ),
    ]
