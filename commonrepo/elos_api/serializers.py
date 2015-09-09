# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from commonrepo.elos.models import ELO
from commonrepo.users.models import User as User

class ELOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ELO
        fields = ('url', 'name', 'fullname', 'author', 'create_date', 'update_date', 'original_type' )
