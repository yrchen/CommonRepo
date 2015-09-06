# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0005_auto_20150907_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='ELOType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of ELO type')),
                ('type_id', models.SmallIntegerField()),
            ],
        ),
    ]
