# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
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
from commonrepo.elos.models import ELO, ELOType, ELOMetadata

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

@api_view(['GET'])
def elos_diversity(request, pk, pk2):
    if request.method == 'GET':
        elo_source = ELO.objects.get(id=pk)
        elo_target = ELO.objects.get(id=pk2)

        # Check user is authenticated and has setting of elo_similarity_threshold
        if request and hasattr(request, "user") and request.user.is_authenticated() and request.user.elo_similarity_threshold:
            elo_diversity = elo_source.diversity(elo_target, request.user.elo_similarity_threshold)
        # if not, use default setting
        else:
            elo_diversity = elo_source.diversity(elo_target, settings.ELO_SIMILARITY_THRESHOLD)

        return Response({"code": status.HTTP_202_ACCEPTED,
                         "status": "ok",
                         "result": {
                             "elo_source": elo_source.id,
                             "elo_target": elo_target.id,
                             "diversity": elo_diversity
                             }
                         },
                        status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def elos_diversity_all(request, pk):
    if request.method == 'GET':
        elo_source = ELO.objects.get(id=pk)
        elos_public = ELO.objects.filter(is_public=1)
        elos_result = {}

        # Check user is authenticated and has setting of elo_similarity_threshold
        if request and hasattr(request, "user") and request.user.is_authenticated() and request.user.elo_similarity_threshold:
            threshold = request.user.elo_similarity_threshold
        # if not, use default setting
        else:
            threshold = settings.ELO_SIMILARITY_THRESHOLD

        for elo in elos_public:
            elos_result.update({elo.id: elo_source.diversity(elo, threshold)})

        return Response({"code": status.HTTP_202_ACCEPTED,
                         "status": "ok",
                         "result": {
                             "elo_source": elo_source.id,
                             "diversity": elos_result
                             }
                         },
                        status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def elos_similarity(request, pk, pk2):
    if request.method == 'GET':
        elo_source = ELO.objects.get(id=pk)
        elo_target = ELO.objects.get(id=pk2)

        # Check user is authenticated and has setting of elo_similarity_threshold
        if request and hasattr(request, "user") and request.user.is_authenticated() and request.user.elo_similarity_threshold:
            elo_similarity = elo_source.similarity(elo_target, request.user.elo_similarity_threshold)
        # if not, use default setting
        else:
            elo_similarity = elo_source.similarity(elo_target, settings.ELO_SIMILARITY_THRESHOLD)

        return Response({"code": status.HTTP_202_ACCEPTED,
                         "status": "ok",
                         "result": {
                             "elo_source": elo_source.id,
                             "elo_target": elo_target.id,
                             "similarity": elo_similarity
                             }
                         },
                        status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def elos_similarity_all(request, pk):
    if request.method == 'GET':
        elo_source = ELO.objects.get(id=pk)
        elos_public = ELO.objects.filter(is_public=1)
        elos_result = {}

        # Check user is authenticated and has setting of elo_similarity_threshold
        if request and hasattr(request, "user") and request.user.is_authenticated() and request.user.elo_similarity_threshold:
            threshold = request.user.elo_similarity_threshold
        # if not, use default setting
        else:
            threshold = settings.ELO_SIMILARITY_THRESHOLD

        for elo in elos_public:
            elos_result.update({elo.id: elo_source.similarity(elo, threshold)})

        return Response({"code": status.HTTP_202_ACCEPTED,
                         "status": "ok",
                         "result": {
                             "elo_source": elo_source.id,
                             "similarity": elos_result
                             }
                         },
                        status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def elos_fork(request, pk):
    if request.method == 'POST':
        elo_original = ELO.objects.get(id=pk)

        if elo_original.is_public:
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

            if elo_original.metadata:
                elo_new_metadata = elo_original.metadata
                elo_new_metadata.pk = None
                elo_new_metadata.save()

                elo_new.metadata = elo_new_metadata

            return Response({"code": status.HTTP_201_CREATED,
                             "status": "ok",
                             "result": {
                                 "elo_id": elo_new.id
                                 }
                            },
                            status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
