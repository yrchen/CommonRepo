# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0018_elometadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='metadata',
            field=models.OneToOneField(null=True, blank=True, to='elos.ELOMetadata'),
        ),
    ]
