# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0028_auto_20151201_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elometadata',
            name='Educational_typicalLearningTime',
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Educational_typicalLearningTime_description',
            field=models.CharField(max_length=255, verbose_name='Educational-typicalLearningTime-description', blank=True),
        ),
        migrations.AddField(
            model_name='elometadata',
            name='Educational_typicalLearningTime_duration',
            field=models.CharField(max_length=255, verbose_name='Educational-typicalLearningTime-duration', blank=True),
        ),
    ]
