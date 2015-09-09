# -*- coding: utf-8 -*-
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

from commonrepo.users.models import User as User
from commonrepo.elos.models import ELO

from .permissions import IsOwnerOrReadOnly
from .serializers import ELOSerializer

class ELOViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents the ELOs in the system.
    """
    queryset = ELO.objects.all()
    serializer_class = ELOSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
