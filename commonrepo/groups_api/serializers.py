# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from commonrepo.groups.models import Group
from commonrepo.users.models import User as User

from .models import GroupFileUpload

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'id', 'name', 'creator', 'create_date', 'create_date','members','description')
        
class GroupSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'id', 'name', 'creator', 'create_date', 'create_date','members','description')
