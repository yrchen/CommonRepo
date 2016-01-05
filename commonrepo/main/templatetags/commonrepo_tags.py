# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import template
from django.conf import settings
from django.contrib.auth import get_user_model

from commonrepo.users.models import User as User

register = template.Library()

# settings value
@register.simple_tag
def get_settings_value(name):
    return getattr(settings, name, "")

@register.simple_tag
def get_user_friends_count(username):
    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    friends_count = user.userprofile.friends.all().count()

    return friends_count

@register.simple_tag
def get_user_followers_count(username):
    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    followers_count = user.followed_by.all().count()

    return followers_count

@register.simple_tag
def get_user_following_count(username):
    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    following_count = user.userprofile.follows.all().count()

    return following_count
