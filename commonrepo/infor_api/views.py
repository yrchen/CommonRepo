# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import authentication
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from rest_framework_tracking.mixins import LoggingMixin

from commonrepo.elos.models import ELO
from commonrepo.users.models import User as User

from .permissions import IsOwnerOrReadOnly

# ELOs
@api_view(['GET'])
def elos_total_count(request):
    if request.method == 'GET':
        return Response({"code": status.HTTP_202_ACCEPTED,
                         "status": "ok",
                         "result": {
                             "total_elos": ELO.objects.all().count()
                             }
                         },
                        status=status.HTTP_202_ACCEPTED)
    else:
        return Response({"code": status.HTTP_400_BAD_REQUEST,
                         "status": "error"
                         },
                        status=status.HTTP_400_BAD_REQUEST)

class InforELOTotalCount(LoggingMixin, APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        if request.method == 'GET':
            return Response({"code": status.HTTP_202_ACCEPTED,
                             "status": "ok",
                             "result": {
                                 "total_elos": ELO.objects.all().count()
                                 }
                             },
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"code": status.HTTP_400_BAD_REQUEST,
                             "status": "error"
                             },
                            status=status.HTTP_400_BAD_REQUEST)

# Users
@api_view(['GET'])
def users_total_count(request):
    if request.method == 'GET':
        return Response({"code": status.HTTP_202_ACCEPTED,
                         "status": "ok",
                         "result": {
                             "total_users": User.objects.all().count()
                             }
                         },
                        status=status.HTTP_202_ACCEPTED)
    else:
        return Response({"code": status.HTTP_400_BAD_REQUEST,
                         "status": "error"
                         },
                        status=status.HTTP_400_BAD_REQUEST)

class InforUsersTotalCount(LoggingMixin, APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        if request.method == 'GET':
            return Response({"code": status.HTTP_202_ACCEPTED,
                             "status": "ok",
                             "result": {
                                 "total_users": User.objects.all().count()
                                 }
                             },
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"code": status.HTTP_400_BAD_REQUEST,
                             "status": "error"
                             },
                            status=status.HTTP_400_BAD_REQUEST)
