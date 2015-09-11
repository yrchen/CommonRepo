# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ELO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of ELO')),
                ('fullname', models.CharField(max_length=255, verbose_name='Full Name of ELO', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('original_type', models.SmallIntegerField()),
                ('author', models.ForeignKey(related_name='elos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ELOType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of ELO type')),
                ('type_id', models.SmallIntegerField()),
            ],
        ),
    ]
