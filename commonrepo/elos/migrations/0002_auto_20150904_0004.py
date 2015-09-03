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
            name='fullname',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='elo',
            name='create_date',
            field=models.DateTimeField(verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='elo',
            name='update_date',
            field=models.DateTimeField(verbose_name=b'date updated'),
        ),
    ]
