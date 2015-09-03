# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0002_auto_20150904_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='fullname',
            field=models.CharField(max_length=255, verbose_name='Full Name of ELO', blank=True),
        ),
        migrations.AlterField(
            model_name='elo',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name of ELO'),
        ),
    ]
