# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elos', '0037_auto_20160107_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reusabilitytree',
            name='name',
            field=models.CharField(max_length=260),
        ),
    ]
