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
View configurations of user information for Users APIs in Common Repo project.
"""

from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from rest_framework_tracking.mixins import LoggingMixin

from commonrepo.users.models import User as User

from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, UserSerializerV2, UserLiteSerializer


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class UserViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the users in the system. (API version 1)

    As you can see, the collection of snippet instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UserViewSetV2(LoggingMixin, viewsets.ModelViewSet):
    """
    This endpoint presents the users in the system. (API version 2)

    As you can see, the collection of ELOs and Groups instances owned by a user
    are serialized using normal model serializer representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializerV2
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserLiteSerializer(queryset, many=True)
        return Response(serializer.data)
