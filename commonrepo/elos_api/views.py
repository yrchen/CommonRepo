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
from commonrepo.elos.models import ELO

from .models import ELOFileUpload
from .permissions import IsOwnerOrReadOnly
from .serializers import ELOSerializer, ELOFileUploadSerializer

class ELOViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the ELOs in the system.
    """
    queryset = ELO.objects.all()
    serializer_class = ELOSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, init_file=self.request.FILES.get('file'))    


class ELOFileUploadViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = ELOFileUpload.objects.all()
    serializer_class = ELOFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                       datafile=sself.request.FILES.get('file'))