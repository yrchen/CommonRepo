# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.CharField(max_length=255, verbose_name='Education', blank=True),
        ),
    ]
