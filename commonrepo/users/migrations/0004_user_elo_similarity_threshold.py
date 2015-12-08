# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151021_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='elo_similarity_threshold',
            field=models.FloatField(default=0, verbose_name='ELOs Similarity Threshold'),
        ),
    ]
