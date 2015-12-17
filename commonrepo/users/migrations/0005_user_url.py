# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_elo_similarity_threshold'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(verbose_name='URL', blank=True),
        ),
    ]
