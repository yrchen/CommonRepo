# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from commonrepo.elos.models import ELO, ELOType
from commonrepo.users.models import User as User

from .models import ELOFileUpload

class ELOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ELO
        fields = ('url', 'id', 'name', 'fullname', 'author', 'create_date', 'update_date', 'original_type', 'is_public', 'init_file', 'version', 'parent_elo', 'parent_elo_version' )

class ELOSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = ELO
        fields = ('url', 'id', 'name', 'fullname', 'author', 'create_date', 'update_date', 'original_type', 'is_public', 'init_file', 'version', 'parent_elo', 'parent_elo_version' )

class ELOTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ELOType
        fields = ('name', 'type_id' )

class ELOFileUploadSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )
    class Meta:
        model = ELOFileUpload
        read_only_fields = ('created', 'datafile', 'owner')