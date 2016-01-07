# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

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
        view=views.follow_user,
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
]
