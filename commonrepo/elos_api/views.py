# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import authentication
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework import views
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FileUploadParser, FormParser, MultiPartParser

from commonrepo.users.models import User as User
from commonrepo.elos.models import ELO, ELOType

from .models import ELOFileUpload
from .permissions import IsOwnerOrReadOnly
from .serializers import ELOSerializer, ELOSerializerV2, ELOTypeSerializer, ELOFileUploadSerializer

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
        
    def perform_update(self, serializer):
        instance = serializer.save()

class ELOViewSetV2(viewsets.ModelViewSet):
    """
    This endpoint presents the ELOs in the system.
    """
    queryset = ELO.objects.all()
    serializer_class = ELOSerializerV2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, init_file=self.request.FILES.get('file'))
        
    def perform_update(self, serializer):
        instance = serializer.save() 

class ELOTypeViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the ELOs in the system.
    """
    queryset = ELOType.objects.all()
    serializer_class = ELOTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user, init_file=self.request.FILES.get('file'))
        
    def perform_update(self, serializer):
        instance = serializer.save()    

class ELOFileUploadViewSet(viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = ELOFileUpload.objects.all()
    serializer_class = ELOFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                       datafile=self.request.FILES.get('file'))

@api_view(['POST'])
def elos_fork(request, pk):
    if request.method == 'POST':
        elo_original = ELO.objects.get(id=pk)
        elo_new = ELO.objects.create(name = elo_original.name + " (Fork from author " + elo_original.author.username + ")",
                                     author = request.user,
                                     original_type = elo_original.original_type,
                                     init_file = elo_original.init_file,
                                     version = 1,
                                     parent_elo = elo_original,
                                     parent_elo_uuid = elo_original.uuid,
                                     parent_elo_version = elo_original.version,
                                     parent_elo2 = elo_original,
                                     parent_elo2_uuid = elo_original.uuid,
                                     parent_elo2_version = elo_original.version)
        return Response({"id": elo_new.id }, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)