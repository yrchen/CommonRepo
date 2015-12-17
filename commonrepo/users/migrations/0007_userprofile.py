# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('follows', models.ManyToManyField(related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(related_name='friend_with', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
