# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from mptt.templatetags import mptt_tags

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from commonrepo.elos.models import ELO, ELOType, ELOMetadata, ReusabilityTree, ReusabilityTreeNode
from commonrepo.users.models import User as User

from .models import ELOFileUpload

class ReusabilityTreeNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReusabilityTreeNode
        exclude = ('id',)

class ReusabilityTreeSerializer(serializers.Serializer):
    nodes = serializers.SerializerMethodField()

    def recursive_node_to_dict(self, node):
        result = {'elo_id': node.elo.id}
        children = [self.recursive_node_to_dict(c) for c in node.get_children()],

        if children is not None:
            result['children'] = children

        return result

    def get_nodes(self, obj):
        root_nodes = mptt_tags.cache_tree_children(obj.root_node.get_descendants(include_self=True))
        dicts = []

        for n in root_nodes:
            dicts.append(self.recursive_node_to_dict(root_nodes[0]))

        return dicts

class ELOMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ELOMetadata
        exclude = ('id',)

class ELOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ELO
        fields = (
            # Basic information
            'url', 'id', 'name', 'fullname', 'author',
            # Metadata
            'create_date', 'update_date', 'original_type', 'is_public', 'init_file',
            # Version control
            'version', 'parent_elo', 'parent_elo_version' )

class ELOSerializerV2(serializers.ModelSerializer):
    metadata = ELOMetadataSerializer(many=False, read_only=True)
    reusability_tree = ReusabilityTreeSerializer(many=False, read_only=True)

    class Meta:
        model = ELO
        fields = (
            # Basic information
            'url', 'id', 'name', 'fullname', 'author',
            # Metadata
            'create_date', 'update_date', 'metadata', 'original_type', 'is_public', 'init_file', 'reusability_tree',
            # Version control
            'version', 'parent_elo', 'parent_elo_version' )


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