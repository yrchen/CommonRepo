# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social_facebook',
            field=models.URLField(max_length=255, verbose_name='Social - Facebook', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='social_google',
            field=models.URLField(max_length=255, verbose_name='Social - Google Plus', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='social_linkedin',
            field=models.URLField(max_length=255, verbose_name='Social - Linkedin', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='social_twitter',
            field=models.URLField(max_length=255, verbose_name='Social - Twitter', blank=True),
        ),
    ]
