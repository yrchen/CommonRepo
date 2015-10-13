# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
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
        regex=r'^all/$',
        view=views.ELOsListView.as_view(),
        name="elos-alllist"
        ),    
    url(
        regex=r'^$',
        view=views.ELOsMyListView.as_view(),
        name='elos-mylist'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.ELOsDetailView.as_view(),
        name='elos-detail'
    ),
    url(
        regex=r'^update/(?P<pk>[0-9]+)/$',
        view=views.ELOsUpdateView.as_view(),
        name='elos-update'
    ),
]
