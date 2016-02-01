# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from licenses.models import License
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
    tree = serializers.SerializerMethodField()

    def recursive_node_to_dict(self, node):
        result = {
            'elo_id': node.elo.id,
            'elo_name': node.elo.name,
            'elo_similarity': node.elo_similarity,
            'elo_diversity': node.elo_diversity,
            'child_elo': [
                self.recursive_node_to_dict(c) for c in node._cached_children
            ]
        }

        return result

    def get_tree(self, obj):
        nodes = mptt_tags.cache_tree_children(
            obj.root_node.get_descendants(include_self=True))
        result = []

        for node in nodes:
            result.append(self.recursive_node_to_dict(node))

        return result


class ELOLicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = License
        exclude = ('is_active', 'organization')


class ELOMetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ELOMetadata
        exclude = ('id',)


class ELOTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ELOType
        fields = ('id', 'name',)


class ELOSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ELO
        fields = (
            # Basic information
            'url', 'id', 'name', 'fullname', 'author', 'description',
            # Metadata
            'create_date', 'update_date', 'original_type', 'is_public', 'init_file',
            # Version control
            'version', 'parent_elo', 'parent_elo_version')


class ELOSerializerV2(serializers.ModelSerializer):
    license = ELOLicenseSerializer(many=False, read_only=True)
    metadata = ELOMetadataSerializer(many=False, read_only=True)
    original_type = ELOTypeSerializer(many=False, read_only=True)
    reusability_tree = ReusabilityTreeSerializer(many=False, read_only=True)

    class Meta:
        model = ELO
        fields = (
            # Basic information
            'url', 'id', 'name', 'fullname', 'author', 'description',
            # Metadata
            'create_date', 'update_date', 'metadata', 'original_type', 'license', 'is_public', 'init_file', 'reusability_tree',
            # Version control
            'version', 'parent_elo', 'parent_elo_version')


class ELOLiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ELO
        fields = (
            # Basic information
            'id', 'name', 'author',
            # Metadata
            'original_type', 'is_public', 'init_file',
            # Version
            'parent_elo')


class ELOFileUploadSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = ELOFileUpload
        read_only_fields = ('created', 'datafile', 'owner')
