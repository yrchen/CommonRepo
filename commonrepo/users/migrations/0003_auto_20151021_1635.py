# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150903_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teaching_category',
            field=models.CharField(max_length=255, verbose_name='Teaching Category', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='teaching_subject_area',
            field=models.CharField(max_length=255, verbose_name='Teaching Subject Area', blank=True),
        ),
    ]
