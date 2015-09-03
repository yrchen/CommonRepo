# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.MyELOsListView.as_view(),
        name='myelos-list'
    ),
    url(
        regex=r'^view/(?P<pk>[0-9]+)/$',
        view=views.MyELOsDetailView.as_view(),
        name='elos-view'
    ),
]
