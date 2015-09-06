# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0003_auto_20150904_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elo',
            name='author',
            field=models.ForeignKey(related_name='elos', to=settings.AUTH_USER_MODEL),
        ),
    ]
