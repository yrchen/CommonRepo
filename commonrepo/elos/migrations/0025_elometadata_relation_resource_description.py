# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0024_auto_20151201_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='elometadata',
            name='Relation_resource_description',
            field=models.CharField(max_length=255, verbose_name='Relation-resource-description', blank=True),
        ),
    ]
