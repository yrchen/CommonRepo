# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from filebrowser.sites import site

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from commonrepo.api.routers import DefaultRouter
from commonrepo.elos_api.views import ELOViewSet, ELOViewSetV2, ELOTypeViewSet, ELOFileUploadViewSet
from commonrepo.elos_api.views import ELODiversity, ELODiversityAll, ELOSimilarity, ELOSimilarityAll, ELOFork
from commonrepo.infor_api.views import InforELOTotalCount, InforUsersTotalCount
from commonrepo.groups_api.views import GroupViewSet, GroupViewSetV2
from commonrepo.groups_api.views import GroupsMemberAbort, GroupsMemberJoin
from commonrepo.main import views as MainViews
from commonrepo.snippets_api.views import SnippetViewSet
from commonrepo.users_api.views import UserViewSet, UserViewSetV2

#
# API v1
#
router_api_v1 = DefaultRouter()
router_api_v1.register(r'api/v1/elos', ELOViewSet)
router_api_v1.register(r'api/v1/elotypes', ELOTypeViewSet)
router_api_v1.register(r'api/v1/groups', GroupViewSet)
router_api_v1.register(r'api/v1/snippets', SnippetViewSet)
router_api_v1.register(r'api/v1/users', UserViewSet)

#
# API v2
#
router_api_v2 = DefaultRouter()
router_api_v2.register(r'api/v2/elos', ELOViewSetV2)
router_api_v2.register(r'api/v2/groups', GroupViewSetV2)
router_api_v2.register(r'api/v2/users', UserViewSetV2)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
    url(r'^download/$', TemplateView.as_view(template_name='pages/download.html'), name="download"),

    url(r'^dashboard/$', MainViews.DashboardView.as_view(), name="dashboard"),

    # Django Admin
    url(r'^admin/filebrowser/', include(site.urls)), # django-filebrowser
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("commonrepo.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),

    # Message
    url(r'^messages/', include('messages_extends.urls')), # django-messages-extends

    # Notifications
    url(r'^notifications/', include('notifications.urls', namespace='notifications')),

    # Activity
    url('^activity/', include('actstream.urls')), # django-activity-stream

    # Comments
    url(r'^comments/', include('fluent_comments.urls')), # django-contrib-comments

    # Your stuff: custom urls includes go here
    url(r'^elos/', include("commonrepo.elos.urls", namespace="elos")),
    url(r'^groups/', include("commonrepo.groups.urls", namespace="groups")),

    # Django REST Framework (DRF) Authenticaion
    url(r'^api/drf/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    #
    # API v1
    #

    # API v1 - Endpoints
    url(r'', include(router_api_v1.urls)),


    # API v1 - Authenticaion
    url(r'^api/v1/auth/', include('djoser.urls.authtoken')),

    # API v1 - ELOs
    url(r'^api/v1/elos-upload', ELOFileUploadViewSet),
    url(r'^api/v1/elos/diversity/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', 'commonrepo.elos_api.views.elos_diversity'),
    url(r'^api/v1/elos/diversity/(?P<pk>[0-9]+)/all/$', 'commonrepo.elos_api.views.elos_diversity_all'),
    url(r'^api/v1/elos/similarity/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', 'commonrepo.elos_api.views.elos_similarity'),
    url(r'^api/v1/elos/similarity/(?P<pk>[0-9]+)/all/$', 'commonrepo.elos_api.views.elos_similarity_all'),
    url(r'^api/v1/elos/fork/(?P<pk>[0-9]+)/$', 'commonrepo.elos_api.views.elos_fork'),

    # API v1 - Information
    url(r'^api/v1/infor/elos-total/$', 'commonrepo.infor_api.views.elos_total_count'),
    url(r'^api/v1/infor/users-total/$', 'commonrepo.infor_api.views.users_total_count'),

    # API v1 - Groups
    url(r'^api/v1/groups/abort/(?P<pk>[0-9]+)/$', 'commonrepo.groups_api.views.groups_member_abort'),
    url(r'^api/v1/groups/join/(?P<pk>[0-9]+)/$', 'commonrepo.groups_api.views.groups_member_join'),

    #
    # API v2
    #

    # API v2 - Endpoints
    url(r'', include(router_api_v2.urls)),

    # API v2 - Authenticaion
    url(r'^api/v2/auth/', include('djoser.urls.authtoken')),

    # API v2 - ELOs
    url(r'^api/v2/elos-upload', ELOFileUploadViewSet),
    url(r'^api/v2/elos/diversity/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', ELODiversity.as_view()),
    url(r'^api/v2/elos/diversity/(?P<pk>[0-9]+)/all/$', ELODiversityAll.as_view()),
    url(r'^api/v2/elos/similarity/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$', ELOSimilarity.as_view()),
    url(r'^api/v2/elos/similarity/(?P<pk>[0-9]+)/all/$', ELOSimilarityAll.as_view()),
    url(r'^api/v2/elos/fork/(?P<pk>[0-9]+)/$', ELOFork.as_view()),

    # API v2 - Information
    url(r'^api/v2/infor/elos-total/$', InforELOTotalCount.as_view()),
    url(r'^api/v2/infor/users-total/$', InforUsersTotalCount.as_view()),

    # API v2 - Groups
    url(r'^api/v2/groups/abort/(?P<pk>[0-9]+)/$', GroupsMemberAbort.as_view()),
    url(r'^api/v2/groups/join/(?P<pk>[0-9]+)/$', GroupsMemberJoin.as_view()),

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
