# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

#from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from commonrepo.api.routers import DefaultRouter
from commonrepo.snippets_api.views import SnippetViewSet
from commonrepo.users_api.views import UserViewSet
from commonrepo.elos_api.views import ELOViewSet, ELOFileUploadViewSet
from commonrepo.groups_api.views import GroupViewSet

router_api = DefaultRouter()
router_api.register(r'api/v1/snippets', SnippetViewSet)
router_api.register(r'api/v1/users', UserViewSet)
router_api.register(r'api/v1/elos', ELOViewSet)
router_api.register(r'api/v1/groups', GroupViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("commonrepo.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^elos/', include("commonrepo.elos.urls", namespace="elos")),
    url(r'^groups/', include("commonrepo.groups.urls", namespace="groups")),

    # API endpoints
    url(r'^', include(router_api.urls)),
    url(r'^api/v0/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/auth/', include('djoser.urls')),
    url(r'^api/v1/auth/token', obtain_auth_token),

    url(r'^api/v1/elos-upload', ELOFileUploadViewSet),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]
