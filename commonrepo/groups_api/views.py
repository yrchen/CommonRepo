# -*- coding: utf-8 -*-
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

from actstream import action

from commonrepo.api.tracking import LoggingMixin
from commonrepo.users.models import User as User
from commonrepo.groups.models import Group

from .permissions import IsOwnerOrReadOnly
from .serializers import GroupSerializer, GroupSerializerV2

class GroupViewSet(LoggingMixin, viewsets.ModelViewSet):
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

class GroupViewSetV2(LoggingMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the Groups in the system.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializerV2
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        group_instance = serializer.save(creator=self.request.user)
        action.send(self.request.user, verb='created', target=group_instance)

    def perform_update(self, serializer):
        group_instance = serializer.save()
        action.send(self.request.user, verb='updated', target=group_instance)

    def perform_destroy(self, instance):
        action.send(self.request.user, verb='deleted', target=instance)
        instance.delete()

@api_view(['POST'])
def groups_member_join(request, pk):
    if request.method == 'POST':
        group = get_object_or_404(Group, id=pk)
        group.members.add(request.user)
        group.save()
        action.send(request.user, verb="joined", target=group)

        return Response({"code": status.HTTP_202_ACCEPTED,
                         "status": "ok",
                         },
                         status=status.HTTP_202_ACCEPTED)
    else:
        return Response({"code": status.HTTP_400_BAD_REQUEST,
                         "status": "error"
                         },
                         status=status.HTTP_400_BAD_REQUEST)

class GroupsMemberJoin(LoggingMixin, APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        if request.method == 'POST':
            group = get_object_or_404(Group, id=pk)
            group.members.add(request.user)
            group.save()
            action.send(request.user, verb="joined", target=group)

            return Response({"code": status.HTTP_202_ACCEPTED,
                             "status": "ok",
                             },
                             status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"code": status.HTTP_400_BAD_REQUEST,
                             "status": "error"
                             },
                             status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def groups_member_abort(request, pk):
    if request.method == 'POST':
        group = get_object_or_404(Group, id=pk)
        group.members.remove(request.user)
        group.save()
        return Response({"code": status.HTTP_202_ACCEPTED,
                         "status": "ok",
                         },
                         status=status.HTTP_202_ACCEPTED)
    else:
        return Response({"code": status.HTTP_400_BAD_REQUEST,
                         "status": "error"
                         },
                         status=status.HTTP_400_BAD_REQUEST)

class GroupsMemberAbort(LoggingMixin, APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        if request.method == 'POST':
            group = get_object_or_404(Group, id=pk)
            group.members.remove(request.user)
            group.save()
            return Response({"code": status.HTTP_202_ACCEPTED,
                             "status": "ok",
                             },
                             status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"code": status.HTTP_400_BAD_REQUEST,
                             "status": "error"
                             },
                             status=status.HTTP_400_BAD_REQUEST)