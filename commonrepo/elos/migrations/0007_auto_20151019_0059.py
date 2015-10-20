# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0006_elo_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='original_type',
            field=models.SmallIntegerField(default=0),
        ),
    ]
