# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

from .snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    # URL pattern for the API
    url(r'^', include(router.urls)),
]
