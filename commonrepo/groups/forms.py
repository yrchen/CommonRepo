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

from django.forms import ModelForm, ModelChoiceField
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from commonrepo.users.models import User as User

from .models import Group


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'creator', 'description', 'logo', 'is_public']

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields["creator"].initial = self.request_user
        self.fields["creator"].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'groups:groups-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))


class GroupAddForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', ]

    def __init__(self, pk=None, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(GroupAddForm, self).__init__(*args, **kwargs)
        group_original = Group.objects.get(id=pk)
        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'groups:groups-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))


class GroupUpdateForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'description', 'logo', 'is_public']

    def __init__(self, pk=None, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'groups:groups-mylist' %}">Cancel</a>"""),
                Submit('save', 'Confirm'),
            ))


class GroupLeaveForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', ]

    def __init__(self, pk=None, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(GroupLeaveForm, self).__init__(*args, **kwargs)
        group_original = Group.objects.get(id=pk)
        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'groups:groups-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
            ))
