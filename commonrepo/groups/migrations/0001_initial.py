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
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of Group')),
                ('fullname', models.CharField(max_length=255, verbose_name='Full Name of Group', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('is_public', models.SmallIntegerField(default=0)),
                ('creator', models.ForeignKey(related_name='commonrepo_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
