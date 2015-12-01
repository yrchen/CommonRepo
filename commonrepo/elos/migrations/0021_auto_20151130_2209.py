# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0020_auto_20151130_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='Classification_taxonPath',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Classification_taxonPath_source',
            field=models.CharField(max_length=255, verbose_name='Classification-taxonPath-source', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Classification_taxonPath_taxon',
            field=models.CharField(max_length=255, verbose_name='Classification-taxonPath-taxon', blank=True),
        ),
    ]
