# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0021_auto_20151130_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='LifeCycle_contribute',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='LifeCycle_contribute_date_dateTime',
            field=models.CharField(max_length=255, verbose_name='LifeCycle-contribute-date-dateTime', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='LifeCycle_contribute_date_description',
            field=models.CharField(max_length=255, verbose_name='LifeCycle-contribute-date-description', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='LifeCycle_contribute_entity',
            field=models.CharField(max_length=255, verbose_name='LifeCycle-contribute-entity', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='LifeCycle_contribute_role',
            field=models.CharField(max_length=255, verbose_name='LifeCycle-contribute-role', blank=True),
        ),
    ]
