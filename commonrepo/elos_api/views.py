# -*- coding: utf-8 -*-

#
# Copyright 2016 edX PDR Lab, National Central University, Taiwan.
#
#     http://edxpdrlab.ncu.cc/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Created By: yrchen@ATCity.org
# Maintained By: yrchen@ATCity.org
#

"""
View configurations of user information for ELOs APIs in Common Repo project.
"""

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import authentication
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework import views
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FileUploadParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework_tracking.mixins import LoggingMixin

from actstream import action
from notifications.signals import notify

from commonrepo.users.models import User as User
from commonrepo.elos.models import ELO, ELOType, ELOMetadata

from .models import ELOFileUpload
from .permissions import IsOwnerOrReadOnly
from .serializers import ELOSerializer, ELOSerializerV2, ELOLiteSerializer, ELOTypeSerializer, ELOFileUploadSerializer


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class ELOViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the ELOs in the system. (API version 1)

    * Requires token authentication.
    """

    queryset = ELO.objects.all()
    serializer_class = ELOSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            init_file=self.request.FILES.get('file'))

    def perform_update(self, serializer):
        instance = serializer.save()


class ELOViewSetV2(LoggingMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the ELOs in the system. (API version 2)

    * Requires token authentication.
    """

    queryset = ELO.objects.all()
    serializer_class = ELOSerializerV2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        elo_instance = serializer.save(
            author=self.request.user,
            init_file=self.request.FILES.get('file'))
        # send action to action stream
        action.send(self.request.user, verb='created', target=elo_instance)

    def perform_update(self, serializer):
        # bumped version
        elo_instance = serializer.save()
        serializer.save(
            author=self.request.user,
            version=elo_instance.version + 1)
        # send action to action stream
        action.send(self.request.user, verb='updated', target=elo_instance)

    def perform_destroy(self, instance):
        # send action to action stream before instance been deleted
        action.send(self.request.user, verb='deleted', target=instance)
        instance.delete()

    def list(self, request):
        # Check the request.user has the permission to access the ELOs
        if request.user and request.user.is_authenticated():
            if request.user.is_staff:
                queryset = ELO.objects.all()
            else:
                queryset = ELO.objects.filter(is_public=1)

            serializer = ELOLiteSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ELOTypeViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the type of ELOs in the system. (API version 1 and 2)

    * Requires token authentication.
    """
    queryset = ELOType.objects.all()
    serializer_class = ELOTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            init_file=self.request.FILES.get('file'))

    def perform_update(self, serializer):
        instance = serializer.save()


class ELOFileUploadViewSet(LoggingMixin, viewsets.ModelViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = ELOFileUpload.objects.all()
    serializer_class = ELOFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        datafile=self.request.FILES.get('file'))


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def elos_diversity(request, pk, pk2):
    """
    Caculate the diversity value of specific ELOs in the system. (API version 1)

    * Requires token authentication.

    Allow Methods:
        GET.

    Keyword Arguments:
        pk (interger):
            The primary key of the source ELO.
        pk2 (interger):
            The primary key of the target ELO

    Returns:
        `Response` objects that representing the result.
    """

    if request.method == 'GET':
        elo_source = get_object_or_404(ELO, id=pk)
        elo_target = get_object_or_404(ELO, id=pk2)

        # Check the user has permission to access the ELOs
        if elo_source.has_permission(
                request.user) and elo_target.has_permission(
                request.user):
            # If user has the setting of elo_similarity_threshold
            if request.user.elo_similarity_threshold:
                elo_diversity = elo_source.diversity(
                    elo_target, request.user.elo_similarity_threshold)
            # if not, use default setting
            else:
                elo_diversity = elo_source.diversity(
                    elo_target, settings.ELO_SIMILARITY_THRESHOLD)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return Response({
            "code": status.HTTP_202_ACCEPTED,
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


class ELODiversity(LoggingMixin, APIView):
    """
    Caculate the diversity value of specific ELOs in the system. (API version 2)

    * Requires token authentication.

    Allow Methods:
        GET.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, pk2):
        """
        Caculate the diversity value of specific ELOs in the system. (API version 2)

        * Requires token authentication.

        Methods:
            GET.

        Keyword Arguments:
            pk (interger):
                The primary key of the source ELO.
            pk2 (interger):
                The primary key of the target ELO

        Returns:
            `Response` objects that representing the result.
        """
        if request.method == 'GET':
            elo_source = get_object_or_404(ELO, pk=pk)
            elo_target = get_object_or_404(ELO, pk=pk2)

            # Check the request.user has permission to access the ELOs
            if elo_source.has_permission(
                    request.user) and elo_target.has_permission(
                    request.user):
                # If user has setting of elo_similarity_threshold
                if request.user.elo_similarity_threshold:
                    elo_diversity = elo_source.diversity(
                        elo_target, request.user.elo_similarity_threshold)
                # if not, use default setting
                else:
                    elo_diversity = elo_source.diversity(
                        elo_target, settings.ELO_SIMILARITY_THRESHOLD)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

            return Response({
                "code": status.HTTP_202_ACCEPTED,
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
@permission_classes((IsAuthenticated, ))
def elos_diversity_all(request, pk):
    """
    Caculate the diversity value of specific ELOs with all ELOs in the system. (API version 1)

    * Requires token authentication.

    Allow Methods:
        GET.

    Keyword Arguments:
        pk (interger):
            The primary key of the ELO.

    Returns:
        `Response` objects that representing the result.
    """

    if request.method == 'GET':
        elo_source = get_object_or_404(ELO, id=pk)
        elos_public = ELO.objects.filter(is_public=1)
        elos_result = {}

        # Check the request.user has permission to access the ELOs
        if elo_source.has_permission(request.user):
            # Check user has setting of elo_similarity_threshold
            if request.user.elo_similarity_threshold:
                threshold = request.user.elo_similarity_threshold
            # if not, use default setting
            else:
                threshold = settings.ELO_SIMILARITY_THRESHOLD
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        for elo in elos_public:
            if elo.has_permission(request.user):
                elos_result.update(
                    {elo.id: elo_source.diversity(elo, threshold)})

        return Response({
            "code": status.HTTP_202_ACCEPTED,
            "status": "ok",
            "result": {
                "elo_source": elo_source.id,
                "diversity": elos_result
                }
            },
            status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ELODiversityAll(LoggingMixin, APIView):
    """
    Caculate the diversity value of specific ELOs with all ELOs in the system. (API version 2)

    * Requires token authentication.

    Allow Methods:
        GET.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        """
        Caculate the diversity value of specific ELOs with all ELOs in the system. (API version 1)

        Methods:
            GET.

        Keyword Arguments:
            pk (interger):
                The primary key of the ELO.

        Returns:
            `Response` objects that representing the result.
        """
        if request.method == 'GET':
            elo_source = get_object_or_404(ELO, id=pk)
            elos_public = ELO.objects.filter(is_public=1)
            elos_result = {}

            # Check the request.user has permission to access the ELOs
            if elo_source.has_permission(request.user):
                # Check user has setting of elo_similarity_threshold
                if request.user.elo_similarity_threshold:
                    threshold = request.user.elo_similarity_threshold
                # if not, use default setting
                else:
                    threshold = settings.ELO_SIMILARITY_THRESHOLD
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

            for elo in elos_public:
                if elo.has_permission(request.user):
                    elos_result.update(
                        {elo.id: elo_source.diversity(elo, threshold)})

            return Response({
                "code": status.HTTP_202_ACCEPTED,
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
@permission_classes((IsAuthenticated, ))
def elos_similarity(request, pk, pk2):
    """
    Caculate the similarity value of specific ELOs in the system. (API version 1)

    * Requires token authentication.

    Allow Methods:
        GET.

    Keyword Arguments:
        pk (interger):
            The primary key of the source ELO.
        pk2 (interger):
            The primart key of the target ELO.

    Returns:
        `Response` objects that representing the result.
    """

    if request.method == 'GET':
        elo_source = get_object_or_404(ELO, id=pk)
        elo_target = get_object_or_404(ELO, id=pk2)

        # Check the request.user has permission to access the ELOs
        if elo_source.has_permission(
                request.user) and elo_target.has_permission(
                request.user):
            # Check user has setting of elo_similarity_threshold
            if request.user.elo_similarity_threshold:
                elo_similarity = elo_source.similarity(
                    elo_target, request.user.elo_similarity_threshold)
            # if not, use default setting
            else:
                elo_similarity = elo_source.similarity(
                    elo_target, settings.ELO_SIMILARITY_THRESHOLD)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return Response({
            "code": status.HTTP_202_ACCEPTED,
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


class ELOSimilarity(LoggingMixin, APIView):
    """
    Caculate the similarity value of specific ELOs in the system. (API version 2)

    * Requires token authentication.

    Allow Methods:
        GET.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, pk2):
        """
        Caculate the similarity value of specific ELOs in the system. (API version 1)

        Methods:
            GET.

        Keyword Arguments:
            pk (interger):
                The primary key of the source ELO.
            pk2 (interger):
                The primart key of the target ELO.

        Returns:
            `Response` objects that representing the result.
        """
        if request.method == 'GET':
            elo_source = get_object_or_404(ELO, id=pk)
            elo_target = get_object_or_404(ELO, id=pk2)

            # Check the request.user has permission to access the ELOs
            if elo_source.has_permission(
                    request.user) and elo_target.has_permission(
                    request.user):
                # Check user has setting of elo_similarity_threshold
                if request.user.elo_similarity_threshold:
                    elo_similarity = elo_source.similarity(
                        elo_target, request.user.elo_similarity_threshold)
                # if not, use default setting
                else:
                    elo_similarity = elo_source.similarity(
                        elo_target, settings.ELO_SIMILARITY_THRESHOLD)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

            return Response({
                "code": status.HTTP_202_ACCEPTED,
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
@permission_classes((IsAuthenticated, ))
def elos_similarity_all(request, pk):
    """
    Caculate the similarity value of specific ELOs with all ELOs in the system. (API version 1)

    * Requires token authentication.

    Allow Methods:
        GET.

    Keyword Arguments:
        pk (interger):
            The primary key of the source ELO.

    Returns:
        `Response` objects that representing the result.
    """

    if request.method == 'GET':
        elo_source = get_object_or_404(ELO, id=pk)
        elos_public = ELO.objects.filter(is_public=1)
        elos_result = {}

        if elo_source.has_permission(request.user):
            # Check user has setting of elo_similarity_threshold
            if request and hasattr(request, "user") and request.user.is_authenticated(
            ) and request.user.elo_similarity_threshold:
                threshold = request.user.elo_similarity_threshold
            # if not, use default setting
            else:
                threshold = settings.ELO_SIMILARITY_THRESHOLD
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        for elo in elos_public:
            if elo.has_permission(request.user):
                elos_result.update(
                    {elo.id: elo_source.similarity(elo, threshold)})

        return Response({
            "code": status.HTTP_202_ACCEPTED,
            "status": "ok",
            "result": {
                "elo_source": elo_source.id,
                "similarity": elos_result
                }
            },
            status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ELOSimilarityAll(LoggingMixin, APIView):
    """
    Caculate the similarity value of the specific ELOs with all ELOs in the system. (API version 2)

    * Requires token authentication.

    Allow Methods:
        GET.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        """
        Caculate the similarity value of the specific ELOs with all ELOs in the system. (API version 2)

        Methods:
            GET.

        Keyword Arguments:
            pk (interger):
                The primary key of the source ELO.

        Returns:
            `Response` objects that representing the result.
        """
        if request.method == 'GET':
            elo_source = get_object_or_404(ELO, id=pk)
            elos_public = ELO.objects.filter(is_public=1)
            elos_result = {}

            if elo_source.has_permission(request.user):
                # Check user has setting of elo_similarity_threshold
                if request and hasattr(request, "user") and request.user.is_authenticated(
                ) and request.user.elo_similarity_threshold:
                    threshold = request.user.elo_similarity_threshold
                # if not, use default setting
                else:
                    threshold = settings.ELO_SIMILARITY_THRESHOLD
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

            for elo in elos_public:
                if elo.has_permission(request.user):
                    elos_result.update(
                        {elo.id: elo_source.similarity(elo, threshold)})

            return Response({
                "code": status.HTTP_202_ACCEPTED,
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
@permission_classes((IsAuthenticated, ))
def elos_fork(request, pk):
    """
    This API used to fork the ELOs in the system. (API version 1)

    * Requires token authentication.

    Allow Methods:
        POST.

    Keyword Arguments:
        pk (interger):
            The primary key of the source ELO.

    Returns:
        `Response` objects that representing the result.
    """

    if request.method == 'POST':
        elo_original = get_object_or_404(ELO, id=pk)

        if elo_original.has_permission(request.user):
            elo_new = ELO.objects.create(
                name=elo_original.name +
                " (Fork from author " +
                elo_original.author.username +
                ")",
                author=request.user,
                description=elo_original.description,
                original_type=elo_original.original_type,
                init_file=elo_original.init_file,
                version=1,
                parent_elo=elo_original,
                parent_elo_uuid=elo_original.uuid,
                parent_elo_version=elo_original.version,
                parent_elo2=elo_original,
                parent_elo2_uuid=elo_original.uuid,
                parent_elo2_version=elo_original.version)

            if elo_original.metadata:
                elo_new_metadata = elo_original.metadata
                elo_new_metadata.pk = None
                elo_new_metadata.save()

                elo_new.metadata = elo_new_metadata
                elo_new.save()

            # send action to action stream
            action.send(request.user, verb='forked', target=elo_new)
            notify.send(
                request.user,
                recipient=elo_original.author,
                verb=u'has forked your ELO',
                level='success')

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


class ELOFork(LoggingMixin, APIView):
    """
    This API used to fork the ELOs in the system. (API version 2)

    * Requires token authentication.

    Allow Methods:
        POST.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        """
        This API used to fork the ELOs in the system. (API version 2)

        * Requires token authentication.

        Methods:
            POST.

        Keyword Arguments:
            pk (interger):
                The primary key of the source ELO.

        Returns:
            `Response` objects that representing the result.
        """        
        if request.method == 'POST':
            elo_original = get_object_or_404(ELO, id=pk)

            if elo_original.has_permission(request.user):
                elo_new = ELO.objects.create(
                    name=elo_original.name +
                    " (forked from author " +
                    elo_original.author.username +
                    ")",
                    author=request.user,
                    description=elo_original.description,
                    original_type=elo_original.original_type,
                    init_file=elo_original.init_file,
                    version=1,
                    parent_elo=elo_original,
                    parent_elo_uuid=elo_original.uuid,
                    parent_elo_version=elo_original.version,
                    parent_elo2=elo_original,
                    parent_elo2_uuid=elo_original.uuid,
                    parent_elo2_version=elo_original.version)

                if elo_original.metadata:
                    elo_new_metadata = elo_original.metadata
                    elo_new_metadata.pk = None
                    elo_new_metadata.save()

                    elo_new.metadata = elo_new_metadata
                    elo_new.save()

                # send action to action stream
                action.send(request.user, verb='forked', target=elo_new)
                notify.send(
                    request.user,
                    recipient=elo_original.author,
                    verb=u'has forked your ELO',
                    level='success')

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
