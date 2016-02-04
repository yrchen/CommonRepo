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

"""
URLs configurations for Users in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals
from django.conf.urls import url

from . import views


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),

    # URL for follow and unfollow user
    url(
        regex=r'^(?P<username>[\w.@+-]+)/follow/$',
        view=views.follow_user,
        name='follow'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/unfollow/$',
        view=views.unfollow_user,
        name='unfollow'
    ),

    # URL for check user's follower and following list
    url(
        regex=r'^(?P<username>[\w.@+-]+)/followers/$',
        view=views.UserFollowerView.as_view(),
        name='followers'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/following/$',
        view=views.UserFollowingView.as_view(),
        name='following'
    ),

    # URL for check user's ELOs
    url(
        regex=r'^(?P<username>[\w.@+-]+)/elos/$',
        view=views.UserELOsListView.as_view(),
        name='elos'
    ),
]
