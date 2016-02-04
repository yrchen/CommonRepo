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
URLs configurations for ELOs in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ELOsMyListView
    url(
        regex=r'^$',
        view=views.ELOsMyListView.as_view(),
        name='elos-mylist'
    ),
    # URL pattern for the ELOsFollowingListView
    url(
        regex=r'^following/$',
        view=views.ELOsFollowingListView.as_view(),
        name='elos-followinglist'
    ),
    # URL pattern for the ELOsDetailView
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.ELOsDetailView.as_view(),
        name='elos-detail'
    ),
    # URL pattern for the ELOsListView
    url(
        regex=r'^all/$',
        view=views.ELOsListView.as_view(),
        name="elos-alllist"
    ),
    # URL pattern for the ELOsCreateView
    url(
        regex=r'^create/$',
        view=views.ELOsCreateView.as_view(),
        name="elos-create"
    ),
    # URL pattern for the ELOsForkView
    url(
        regex=r'^fork/(?P<pk>[0-9]+)/$',
        view=views.ELOsForkView.as_view(),
        name="elos-fork"
    ),
    # URL pattern for the ELOsNetworkView
    url(
        regex=r'^netork/(?P<pk>[0-9]+)/$',
        view=views.ELOsNetworkView.as_view(),
        name="elos-network"
    ),
    # URL pattern for the ELOsUpdateView
    url(
        regex=r'^update/(?P<pk>[0-9]+)/$',
        view=views.ELOsUpdateView.as_view(),
        name='elos-update'
    ),
    # URL pattern for the ELOTypesDetailView
    url(
        regex=r'^type/(?P<pk>[0-9]+)/$',
        view=views.ELOTypesDetailView.as_view(),
        name='elotypes-detail'
    ),
    # URL pattern for the publish ELO action
    url(
        regex=r'^publish/(?P<pk>[0-9]+)/$',
        view=views.publish_elo,
        name='elos-publish'
    ),
    # URL pattern for the unpublish ELO action
    url(
        regex=r'^unpublish/(?P<pk>[0-9]+)/$',
        view=views.unpublish_elo,
        name='elos-unpublish'
    ),
    # URL pattern for the follow ELO action
    url(
        regex=r'^follow/(?P<pk>[0-9]+)/$',
        view=views.follow_elo,
        name='elos-follow'
    ),
    # URL pattern for the unfollow ELO action
    url(
        regex=r'^unfollow/(?P<pk>[0-9]+)/$',
        view=views.unfollow_elo,
        name='elos-unfollow'
    )
]
