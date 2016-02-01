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
