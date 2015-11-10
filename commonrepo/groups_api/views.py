# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import authentication
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import views
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FileUploadParser, FormParser, MultiPartParser

from commonrepo.users.models import User as User
from commonrepo.groups.models import Group

from .models import GroupFileUpload
from .permissions import IsOwnerOrReadOnly
from .serializers import GroupSerializer, GroupSerializerV2, GroupFileUploadSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the Groups in the system.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()

class GroupViewSetV2(viewsets.ModelViewSet):
    """
    This endpoint presents the Groups in the system.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializerV2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()

class GroupFileUploadViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = GroupFileUpload.objects.all()
    serializer_class = GroupFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                       datafile=self.request.FILES.get('file'))
