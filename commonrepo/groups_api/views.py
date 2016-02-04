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
View configurations of user information for Groups APIs in Common Repo project.
"""

from __future__ import absolute_import, unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
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
from rest_framework.views import APIView

from rest_framework_tracking.mixins import LoggingMixin

from actstream import action
from notifications.signals import notify

from commonrepo.users.models import User as User
from commonrepo.groups.models import Group

from .permissions import IsOwnerOrReadOnly
from .serializers import GroupSerializer, GroupSerializerV2


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class GroupViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the Groups in the system. (API version 1)

    * Requires token authentication.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()


class GroupViewSetV2(LoggingMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the Groups in the system. (API version 2)

    * Requires token authentication.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializerV2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        group_instance = serializer.save(creator=self.request.user)
        # send action to action stream
        action.send(self.request.user, verb='created', target=group_instance)

    def perform_update(self, serializer):
        group_instance = serializer.save()
        # send action to action stream
        action.send(self.request.user, verb='updated', target=group_instance)

    def perform_destroy(self, instance):
        # send action to action stream before instance been deleted
        action.send(self.request.user, verb='deleted', target=instance)
        instance.delete()


@api_view(['POST'])
def groups_member_join(request, pk):
    """
    This API used to allow user to join the specific Groups in the system. (API version 1)

    * Requires token authentication.
    """

    if request.method == 'POST':
        group = get_object_or_404(Group, id=pk)
        group.members.add(request.user)
        group.save()
        # send action to action stream
        action.send(request.user, verb="joined", target=group)
        notify.send(
            request.user,
            recipient=group.creator,
            verb=u'has joined to your Group',
            level='success')

        return Response({
            "code": status.HTTP_202_ACCEPTED,
            "status": "ok",
            },
            status=status.HTTP_202_ACCEPTED)
    else:
        return Response({
            "code": status.HTTP_400_BAD_REQUEST,
            "status": "error"
            },
            status=status.HTTP_400_BAD_REQUEST)


class GroupsMemberJoin(LoggingMixin, APIView):
    """
    This API used to allow user to join the specific Groups in the system. (API version 2)

    * Requires token authentication.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        if request.method == 'POST':
            group = get_object_or_404(Group, id=pk)
            group.members.add(request.user)
            group.save()
            # send action to action stream
            action.send(request.user, verb="joined", target=group)
            notify.send(
                request.user,
                recipient=group.creator,
                verb=u'has joined to your Group',
                level='success')

            return Response({
                "code": status.HTTP_202_ACCEPTED,
                "status": "ok",
                },
                status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                "code": status.HTTP_400_BAD_REQUEST,
                "status": "error"
                },
                status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def groups_member_abort(request, pk):
    """
    This API used to allow user to abort the specific Groups in the system. (API version 1)

    * Requires token authentication.
    """

    if request.method == 'POST':
        group = get_object_or_404(Group, id=pk)
        group.members.remove(request.user)
        group.save()
        # send action to action stream
        action.send(request.user, verb="aborted", target=group)
        notify.send(
            request.user,
            recipient=group.creator,
            verb=u'has aborted from your Group',
            level='success')

        return Response({
            "code": status.HTTP_202_ACCEPTED,
            "status": "ok",
            },
            status=status.HTTP_202_ACCEPTED)
    else:
        return Response({
            "code": status.HTTP_400_BAD_REQUEST,
            "status": "error"
            },
            status=status.HTTP_400_BAD_REQUEST)


class GroupsMemberAbort(LoggingMixin, APIView):
    """
    This API used to allow user to abort the specific Groups in the system. (API version 2)

    * Requires token authentication.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        if request.method == 'POST':
            group = get_object_or_404(Group, id=pk)
            group.members.remove(request.user)
            group.save()
            # send action to action stream
            action.send(request.user, verb="aborted", target=group)
            notify.send(
                request.user,
                recipient=group.creator,
                verb=u'has aborted from your Group',
                level='success')

            return Response({
                "code": status.HTTP_202_ACCEPTED,
                "status": "ok",
                },
                status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                "code": status.HTTP_400_BAD_REQUEST,
                "status": "error"
                },
                status=status.HTTP_400_BAD_REQUEST)
