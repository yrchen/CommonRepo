# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0041_auto_20160201_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='metadata',
            field=annoying.fields.AutoOneToOneField(null=True, to='elos.ELOMetadata'),
        ),
    ]
