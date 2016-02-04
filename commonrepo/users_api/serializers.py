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
Serializer of user information in Common Repo project.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from commonrepo.groups.models import Group as Group
from commonrepo.users.models import User as User

from commonrepo.elos.models import ELO
from commonrepo.snippets_api.models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of user information. (API version 1)

    A serializer containing all information about a user needed by clients.
    Because these pieces of information reside in different tables, this is
    designed to work well with prefetch_related and select_related, which
    require the use of all() instead of get() or filter(). The following fields
    should be prefetched on the user objects being serialized:
     * profile
     * preferences
     * elos
     * groups
    """

    class Meta:
        model = User
        fields = (
            # Basic user information
            'url',
            'id',
            'username',
            'organization',
            'education',
            'url',
            'phone',
            'address',
            'language',
            'area',
            'about',
            # Extend user information
            'teaching_category',
            'teaching_subject_area',
            # ELO related information
            'elo_similarity_threshold',
            'elos',
            'elos_published',
            'elos_forks',
            'elos_from_others',
            # Group information
            'commonrepo_groups',
            'commonrepo_groups_members',
            # Misc
            'snippets', )

    # ELOs information
    # elos = ForeignKey relationship from model ELO.author
    elos_published = serializers.SerializerMethodField()
    elos_forks = serializers.SerializerMethodField()
    elos_from_others = serializers.SerializerMethodField()

    # Groups
    # commonrepo_groups = ForeignKey relationship from model Group.creator

    # Misc
    # snippets = ForeignKey relationship from model snippets.owner

    # Caculate the number of published ELOs of user
    def get_elos_published(self, obj):
        request = self.context.get("request")

        if request and hasattr(request,
                               "user") and request.user.is_authenticated():
            return ELO.objects.filter(
                author=request.user).filter(
                is_public=1).count()
        else:
            return -1

    # Caculate the number of forked ELOs of user
    def get_elos_forks(self, obj):
        request = self.context.get("request")
        total_forks = 0

        if request and hasattr(request,
                               "user") and request.user.is_authenticated():
            my_elo_sets = ELO.objects.filter(author=request.user)

            for elo in my_elo_sets:
                total_forks += ELO.objects.filter(parent_elo=elo.id).count()

            return total_forks

        else:
            return -1

    # Caculate the number of forked ELOs from other users
    def get_elos_from_others(self, obj):
        request = self.context.get("request")

        if request and hasattr(request,
                               "user") and request.user.is_authenticated():
            my_elo_count = ELO.objects.filter(
                author=request.user).filter(
                is_public=1).count()
            my_original_elo_count = ELO.objects.filter(
                author=request.user).filter(
                is_public=1).filter(
                parent_elo=1).count()
            return my_elo_count - my_original_elo_count

        else:
            return -1


class UserSerializerV2(serializers.ModelSerializer):
    """
    Serializer of user information. (API version 2)

    A serializer containing all information about a user needed by clients.
    Because these pieces of information reside in different tables, this is
    designed to work well with prefetch_related and select_related, which
    require the use of all() instead of get() or filter(). The following fields
    should be prefetched on the user objects being serialized:
     * profile
     * preferences
     * elos
     * groups
    """

    class Meta:
        model = User
        fields = (
            # Basic user information
            'url',
            'id',
            'username',
            'organization',
            'education',
            'url',
            'phone',
            'address',
            'language',
            'area',
            'about',
            # Social informaion
            'social_facebook',
            'social_google',
            'social_linkedin',
            'social_twitter',
            # Extend user information
            'teaching_category',
            'teaching_subject_area',
            # Social information
            'friend_with',
            'followed_by',
            # ELO related information
            'elo_similarity_threshold',
            'elos',
            'elos_published',
            'elos_forks',
            'elos_from_others',
            # Group information
            'commonrepo_groups',
            'commonrepo_groups_members',
            # Misc
            'snippets',
            # Preferences
            'elo_similarity_threshold',)

    # ELOs information
    # elos = ForeignKey relationship from model ELO.author
    elos_published = serializers.SerializerMethodField()
    elos_forks = serializers.SerializerMethodField()
    elos_from_others = serializers.SerializerMethodField()

    # Groups
    # commonrepo_groups = ForeignKey relationship from model Group.creator

    # Misc
    # snippets = ForeignKey relationship from model snippets.owner

    # Caculate the number of published ELOs of user
    def get_elos_published(self, obj):
        request = self.context.get("request")

        if request and hasattr(request,
                               "user") and request.user.is_authenticated():
            return ELO.objects.filter(author=obj).filter(is_public=1).count()
        else:
            return -1

    # Caculate the number of forked ELOs of user
    def get_elos_forks(self, obj):
        request = self.context.get("request")
        total_forks = 0

        if request and hasattr(request,
                               "user") and request.user.is_authenticated():
            my_elo_sets = ELO.objects.filter(author=obj)

            for elo in my_elo_sets:
                total_forks += ELO.objects.filter(parent_elo=elo.id).count()

            return total_forks

        else:
            return -1

    # Caculate the number of forked ELOs from other users
    def get_elos_from_others(self, obj):
        request = self.context.get("request")

        if request and hasattr(request,
                               "user") and request.user.is_authenticated():
            my_elo_count = ELO.objects.filter(
                author=obj).filter(
                is_public=1).count()
            my_original_elo_count = ELO.objects.filter(
                author=obj).filter(
                is_public=1).filter(
                parent_elo=1).count()
            return my_elo_count - my_original_elo_count

        else:
            return -1


class UserLiteSerializer(serializers.ModelSerializer):
    """
    Serializer of lite user information. (API version 2)

    This serializer provides fewer information than the previous serializers.
    Only been used for user list requests.

    A serializer containing all information about a user needed by clients.
    Because these pieces of information reside in different tables, this is
    designed to work well with prefetch_related and select_related, which
    require the use of all() instead of get() or filter(). The following fields
    should be prefetched on the user objects being serialized:
     * profile
     * preferences
     * elos
     * groups
    """

    class Meta:
        model = User
        fields = (
            # Basic user information
            'id',
            'username',
            'organization',
            'education',
            'url',
            'phone',
            'address',
            'language',
            'area',
            'about',
            # Social informaion
            'social_facebook',
            'social_google',
            'social_linkedin',
            'social_twitter',
            # Extend user information
            'teaching_category',
            'teaching_subject_area', )
