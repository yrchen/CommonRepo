# -*- coding: utf-8 -*-
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
    url(
        regex=r'^following/$',
        view=views.ELOsFollowingListView.as_view(),
        name='elos-followinglist'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.ELOsDetailView.as_view(),
        name='elos-detail'
    ),
    url(
        regex=r'^all/$',
        view=views.ELOsListView.as_view(),
        name="elos-alllist"
    ),
    url(
        regex=r'^create/$',
        view=views.ELOsCreateView.as_view(),
        name="elos-create"
    ),
    url(
        regex=r'^fork/(?P<pk>[0-9]+)/$',
        view=views.ELOsForkView.as_view(),
        name="elos-fork"
    ),
    url(
        regex=r'^netork/(?P<pk>[0-9]+)/$',
        view=views.ELOsNetworkView.as_view(),
        name="elos-network"
    ),
    url(
        regex=r'^update/(?P<pk>[0-9]+)/$',
        view=views.ELOsUpdateView.as_view(),
        name='elos-update'
    ),
    url(
        regex=r'^type/(?P<pk>[0-9]+)/$',
        view=views.ELOTypesDetailView.as_view(),
        name='elotypes-detail'
    ),

    # Publish ELO
    url(
        regex=r'^publish/(?P<pk>[0-9]+)/$',
        view=views.publish_elo,
        name='elos-publish'
    ),
    # Unpublish ELO
    url(
        regex=r'^unpublish/(?P<pk>[0-9]+)/$',
        view=views.unpublish_elo,
        name='elos-unpublish'
    ),

    # Follow ELO
    url(
        regex=r'^follow/(?P<pk>[0-9]+)/$',
        view=views.follow_elo,
        name='elos-follow'
    ),
    # Unfollow ELO
    url(
        regex=r'^unfollow/(?P<pk>[0-9]+)/$',
        view=views.unfollow_elo,
        name='elos-unfollow'
    )
]
