# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0030_auto_20151201_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reusabilitytree',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reusabilitytreenode',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
