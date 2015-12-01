# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0027_auto_20151201_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='Annotation_date',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Annotation_date_dateTime',
            field=models.CharField(max_length=255, verbose_name='Annotation-date_dateTime', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Annotation_date_description',
            field=models.CharField(max_length=255, verbose_name='Annotation-date-description', blank=True),
        ),
    ]
