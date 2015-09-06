# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0004_auto_20150907_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='elo',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
    ]
