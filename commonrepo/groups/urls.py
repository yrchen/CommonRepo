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
URLs configurations for Groups in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the GroupsAbortView
    url(
        regex=r'^abort/(?P<pk>[0-9]+)/$',
        view=views.GroupsAbortView.as_view(),
        name="groups-abort"
    ),
    # URL pattern for the GroupsListView
    url(
        regex=r'^all/$',
        view=views.GroupsListView.as_view(),
        name="groups-alllist"
    ),
    # URL pattern for the GroupsCreateView
    url(
        regex=r'^create/$',
        view=views.GroupsCreateView.as_view(),
        name="groups-create"
    ),
    # URL pattern for the GroupsDetailView
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.GroupsDetailView.as_view(),
        name='groups-detail'
    ),
    # URL pattern for the GroupsJoinView
    url(
        regex=r'^join/(?P<pk>[0-9]+)/$',
        view=views.GroupsJoinView.as_view(),
        name="groups-join"
    ),
    # URL pattern for the GroupsMyListView
    url(
        regex=r'^$',
        view=views.GroupsMyListView.as_view(),
        name='groups-mylist'
    ),
    # URL pattern for the GroupsFollowingListView
    url(
        regex=r'^following/$',
        view=views.GroupsFollowingListView.as_view(),
        name='groups-followinglist'
    ),
    # URL pattern for the GroupsUpdateView
    url(
        regex=r'^update/(?P<pk>[0-9]+)/$',
        view=views.GroupsUpdateView.as_view(),
        name='groups-update'
    ),
    # URL pattern for the follow Group action
    url(
        regex=r'^follow/(?P<pk>[0-9]+)/$',
        view=views.follow_group,
        name='groups-follow'
    ),
    # URL pattern for the unfollow Group action
    url(
        regex=r'^unfollow/(?P<pk>[0-9]+)/$',
        view=views.unfollow_group,
        name='groups-unfollow'
    ),
]
