# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

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
        fields = ['name', 'creator', ]

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields["creator"].initial = self.request_user
        self.fields["creator"].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'groups:groups-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))

class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name','members']

    def __init__(self, pk=None,*args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(GroupAddForm, self).__init__(*args, **kwargs)
        group_original = Group.objects.get(id=pk)
        self.fields["members"].initial = group_original.members.add(self.request_user)
        self.fields["members"].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'groups:groups-mylist' %}">Confirm</a>"""),
#                Submit('save', 'Submit'),
        ))

class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'members' ]

    def __init__(self, pk=None, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'groups:groups-mylist' %}">Confirm</a>"""),
#                Submit('save', 'Submit'),
        ))
