# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from commonrepo.users.models import User as User

from commonrepo.elos.models import ELO
from commonrepo.snippets_api.models import Snippet

class UserSerializer(serializers.HyperlinkedModelSerializer):
    elos = serializers.HyperlinkedRelatedField(queryset=ELO.objects.all(), view_name='elos:elos-detail', many=True)
    snippets = serializers.HyperlinkedRelatedField(queryset=Snippet.objects.all(), view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'organization', 'phone', 'address', 'language', 'area', 'teaching_category', 'teaching_subject_area', 'elos', 'snippets', )
