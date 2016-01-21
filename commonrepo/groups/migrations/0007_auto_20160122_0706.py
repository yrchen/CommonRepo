# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import commonrepo.groups.models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_group_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='logo',
            field=models.ImageField(upload_to=commonrepo.groups.models.groups_get_random_filename, verbose_name='Logo of Group', blank=True),
        ),
    ]
