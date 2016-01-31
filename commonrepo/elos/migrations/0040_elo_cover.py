# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import commonrepo.elos.models


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0039_auto_20160122_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='cover',
            field=models.ImageField(upload_to=commonrepo.elos.models.elos_get_cover_filename, verbose_name='Cover of ELO', blank=True),
        ),
    ]
