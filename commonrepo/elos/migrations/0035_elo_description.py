# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0034_auto_20151219_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Description of ELO', blank=True),
        ),
    ]
