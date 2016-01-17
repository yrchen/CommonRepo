# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0038_auto_20160107_2320'),
        ('users', '0009_auto_20151228_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='follow_elos',
            field=models.ManyToManyField(related_name='followed_by', to='elos.ELO'),
        ),
    ]
