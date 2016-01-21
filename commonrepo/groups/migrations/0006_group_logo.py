# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('groups', '0005_auto_20160121_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='logo',
            field=filer.fields.image.FilerImageField(related_name='group_logo', blank=True, to='filer.Image', null=True),
        ),
    ]
