# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from commonrepo.elos.models import ELO
from commonrepo.users.models import User as User

from .permissions import IsOwnerOrReadOnly

# ELOs
@api_view(['GET'])
def elos_total_count(request):
    if request.method == 'GET':
        return Response({"total_elos": ELO.objects.all().count() }, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)    

# Users
@api_view(['GET'])
def users_total_count(request):
    if request.method == 'GET':
        return Response({"total_users": User.objects.all().count() }, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)  