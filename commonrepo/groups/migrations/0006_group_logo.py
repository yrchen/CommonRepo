# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20160121_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='logo',
            field=models.ImageField(upload_to='groups/', verbose_name='Logo of Group', blank=True),
        ),
    ]
