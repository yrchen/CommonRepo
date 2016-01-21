# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import commonrepo.elos.models


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0038_auto_20160107_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='init_file',
            field=models.FileField(default='', upload_to=commonrepo.elos.models.elos_get_random_filename, blank=True),
        ),
    ]
