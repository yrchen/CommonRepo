# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0019_elo_metadata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='Relation_resource',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Relation_resource_identifier_catalog',
            field=models.CharField(max_length=255, verbose_name='Relation-resource-identifier-catalog', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Relation_resource_identifier_entry',
            field=models.CharField(max_length=255, verbose_name='Relation-resource-identifier-entry', blank=True),
        ),
    ]
