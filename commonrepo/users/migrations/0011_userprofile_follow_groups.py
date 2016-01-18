# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_group_members'),
        ('users', '0010_userprofile_follow_elos'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='follow_groups',
            field=models.ManyToManyField(related_name='followed_by', to='groups.Group'),
        ),
    ]
