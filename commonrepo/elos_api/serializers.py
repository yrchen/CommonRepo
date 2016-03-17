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
Serializer of group information in Common Repo project.
"""

from __future__ import absolute_import, unicode_literals

from licenses.models import License
from mptt.templatetags import mptt_tags

from rest_framework import serializers

from commonrepo.elos.models import ELO, ELOType, ELOMetadata, ReusabilityTreeNode

from .models import ELOFileUpload


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class ReusabilityTreeNodeSerializer(serializers.ModelSerializer):
    """
    Serializer of ReusabilityTreeNode
    """

    class Meta:
        model = ReusabilityTreeNode
        exclude = ('id',)


class ReusabilityTreeSerializer(serializers.Serializer):
    """
    Serializer of ReusabilityTree
    """
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
    """
    Serializer of ELO License
    """

    class Meta:
        model = License
        exclude = ('is_active', 'organization')


class ELOMetadataSerializer(serializers.ModelSerializer):
    """
    Serializer of ELO Metadata
    """

    class Meta:
        model = ELOMetadata
        exclude = ('id',)


class ELOTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of ELOType
    """

    class Meta:
        model = ELOType
        fields = ('id', 'name',)


class ELOSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of ELO
    """

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
    """
    Serializer of ELO (version 2)
    """

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
    """
    Serializer of ELO (lite version)

    This serializer provides fewer information than the `ELOSerializerV2`.
    """

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
