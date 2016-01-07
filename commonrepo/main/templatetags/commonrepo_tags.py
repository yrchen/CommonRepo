# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import template
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from commonrepo.elos.models import ELO
from commonrepo.groups.models import Group
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

@register.simple_tag
def get_user_elo_count(username):
    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    elo_count = ELO.objects.filter(author=user).filter(is_public=1).count()

    return elo_count

@register.simple_tag
def get_user_group_count(username):
    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    group_count = Group.objects.filter(creator=user).count()

    return group_count

@register.simple_tag
def commonrepo_display_action(action_instance):
    templates = 'misc/action.html'

    return render_to_string(templates, {'action': action_instance})