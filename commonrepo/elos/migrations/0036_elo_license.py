# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '__first__'),
        ('elos', '0035_elo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='license',
            field=models.ForeignKey(related_name='elos', blank=True, to='licenses.License', null=True),
        ),
    ]
