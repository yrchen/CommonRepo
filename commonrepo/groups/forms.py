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
        fields = ['name', 'creator']

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))

class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'is_public']

    def __init__(self, pk=None, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))
