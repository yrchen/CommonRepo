# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0022_auto_20151130_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='elometadata',
            name='Classification_taxonPath_taxon_entry',
            field=models.CharField(max_length=255, verbose_name='Classification-taxonPath-taxon-entry', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Classification_taxonPath_taxon_id',
            field=models.CharField(max_length=255, verbose_name='Classification-taxonPath-taxon-id', blank=True),
        ),
    ]
