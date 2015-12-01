# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0026_auto_20151201_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='Meta_metadata_contribute_date',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Meta_metadata_contribute_date_dateTime',
            field=models.CharField(max_length=255, verbose_name='Meta-metadata-contribute-date-dateTime', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Meta_metadata_contribute_date_description',
            field=models.CharField(max_length=255, verbose_name='Meta-metadata-contribute-date-description', blank=True),
        ),
    ]
