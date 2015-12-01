# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0023_auto_20151201_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='Meta_metadata_contribute',
        ),
        migrations.RemoveField(
            model_name='elometadata',
            name='Meta_metadata_identifier',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Meta_metadata_contribute_date',
            field=models.CharField(max_length=255, verbose_name='Meta-metadata-contribute-date', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Meta_metadata_contribute_entity',
            field=models.CharField(max_length=255, verbose_name='Meta-metadata-contribute-entity', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Meta_metadata_contribute_role',
            field=models.CharField(max_length=255, verbose_name='Meta-metadata-contribute-role', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Meta_metadata_identifier_catalog',
            field=models.CharField(max_length=255, verbose_name='Meta_metadata-identifier-catalog', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Meta_metadata_identifier_entry',
            field=models.CharField(max_length=255, verbose_name='Meta_metadata-identifier-entry', blank=True),
        ),
    ]
