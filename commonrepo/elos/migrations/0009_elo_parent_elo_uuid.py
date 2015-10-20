# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0008_elo_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='elo',
            name='parent_elo_uuid',
            field=models.UUIDField(default=uuid.uuid4, blank=True),
        ),
    ]
