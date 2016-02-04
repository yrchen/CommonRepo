# -*- coding: utf-8 -*-

#
# Copyright 2016 edX PDR Lab, National Central University, Taiwan.
#
#     http://edxpdrlab.ncu.cc/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Created By: yrchen@ATCity.org
# Maintained By: yrchen@ATCity.org
#

from __future__ import absolute_import, unicode_literals

from django import template
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from commonrepo.elos.models import ELO
from commonrepo.groups.models import Group
from commonrepo.users.models import User as User

register = template.Library()


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


@register.simple_tag
def get_settings_value(name):
    '''
    Return settins value in templates.
    '''

    return getattr(settings, name, "")


@register.simple_tag
def get_user_friends_count(username):
    '''
    Return friends count of specific user.
    '''

    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    friends_count = user.userprofile.friends.all().count()

    return friends_count


@register.simple_tag
def get_user_followers_count(username):
    '''
    Return followers count of specific user.
    '''

    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    followers_count = user.followed_by.all().count()

    return followers_count


@register.simple_tag
def get_user_following_count(username):
    '''
    Return following count of specific user.
    '''

    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    following_count = user.userprofile.follows.all().count()

    return following_count


@register.simple_tag
def get_user_elo_count(username):
    '''
    Return ELO count of specific user.
    '''

    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    elo_count = ELO.objects.filter(author=user).filter(is_public=1).count()

    return elo_count


@register.simple_tag
def get_user_group_count(username):
    '''
    Return joined group count of specific user.
    '''

    try:
        user = User.objects.get_by_natural_key(username)
    except DoesNotExist:
        return 0

    group_count = Group.objects.filter(creator=user).count()

    return group_count


@register.simple_tag
def commonrepo_display_action(action_instance):
    '''
    Display actions in Common Repo own style.
    '''

    templates = 'misc/action.html'

    return render_to_string(templates, {'action': action_instance})
