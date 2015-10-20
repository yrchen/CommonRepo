# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0005_auto_20151014_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='is_public',
            field=models.SmallIntegerField(default=0),
        ),
    ]
