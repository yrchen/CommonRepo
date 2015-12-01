# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0029_auto_20151201_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='Technical_duration',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Technical_duration_description',
            field=models.CharField(max_length=255, verbose_name='Technical-duration-description', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Technical_duration_duration',
            field=models.CharField(max_length=255, verbose_name='Technical-duration-duration', blank=True),
        ),
    ]
