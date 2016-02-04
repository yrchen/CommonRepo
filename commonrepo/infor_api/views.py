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


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


@api_view(['GET'])
def elos_total_count(request):
    """
    This API used to get the total ELOs count in the system. (API version 1)

    * Requires token authentication.
    """

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
    This API used to get the total ELOs count in the system. (API version 2)

    * Requires token authentication.
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
    """
    This API used to get the total users count in the system. (API version 1)

    * Requires token authentication.
    """

    if request.method == 'GET':
        return Response({
            "code": status.HTTP_202_ACCEPTED,
            "status": "ok",
            "result": {
                "total_users": User.objects.all().count()
                }
            },
            status=status.HTTP_202_ACCEPTED)
    else:
        return Response({
            "code": status.HTTP_400_BAD_REQUEST,
            "status": "error"
            },
            status=status.HTTP_400_BAD_REQUEST)


class InforUsersTotalCount(LoggingMixin, APIView):
    """
    This API used to get the total users count in the system. (API version 2)

    * Requires token authentication.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        if request.method == 'GET':
            return Response({
                "code": status.HTTP_202_ACCEPTED,
                "status": "ok",
                "result": {
                    "total_users": User.objects.all().count()
                    }
                },
                status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                "code": status.HTTP_400_BAD_REQUEST,
                "status": "error"
                },
                status=status.HTTP_400_BAD_REQUEST)
