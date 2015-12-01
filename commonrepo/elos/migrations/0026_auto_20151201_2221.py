# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0025_elometadata_relation_resource_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='Technical_requirement',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Technical_requirement_orComposite_maximumVersion',
            field=models.CharField(max_length=255, verbose_name='Technical-requirement-orComposite-maximumVersion', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Technical_requirement_orComposite_minimumVersion',
            field=models.CharField(max_length=255, verbose_name='Technical-requirement-orComposite-minimumVersion', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Technical_requirement_orComposite_name',
            field=models.CharField(max_length=255, verbose_name='Technical-requirement-orComposite-name', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Technical_requirement_orComposite_type',
            field=models.CharField(max_length=255, verbose_name='Technical-requirement-orComposite-type', blank=True),
        ),
    ]
