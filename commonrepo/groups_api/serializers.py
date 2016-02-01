# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from commonrepo.groups.models import Group
from commonrepo.users.models import User as User


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = (
            'url',
            'id',
            'name',
            'creator',
            'description',
            'create_date',
            'update_date',
            'members',
        )


class GroupSerializerV2(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'url',
            'id',
            'name',
            'creator',
            'description',
            'create_date',
            'update_date',
            'members',
        )
