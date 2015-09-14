# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='init_file',
            field=models.FileField(default='', upload_to=b'', blank=True),
        ),
    ]
