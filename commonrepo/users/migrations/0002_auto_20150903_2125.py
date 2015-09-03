# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Address', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='area',
            field=models.CharField(max_length=255, verbose_name='Area/Nation', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(max_length=255, verbose_name='Language', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.CharField(max_length=255, verbose_name='Organization/School', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Phone nubmer', blank=True),
        ),
    ]
