# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0036_elo_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reusabilitytreenode',
            name='name',
            field=models.CharField(max_length=260),
        ),
    ]
