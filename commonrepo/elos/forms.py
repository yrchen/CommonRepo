# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.forms import ModelForm, ModelChoiceField
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from commonrepo.users.models import User as User

from .models import ELO

class ELOForm(ModelForm):
    class Meta:
        model = ELO
        fields = ['name', 'author', 'description', 'original_type', 'license', 'init_file']

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(ELOForm, self).__init__(*args, **kwargs)

        # check if user is not staff
        if not self.request_user.is_staff:
            self.fields["author"].queryset = User.objects.filter(username=self.request_user)
            self.fields["author"].widget.attrs['readonly'] = True

        # author can't be empty
        self.fields["author"].empty_label = None

        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))

class ELOForkForm(ModelForm):
    class Meta:
        model = ELO
        fields = ['name', 'author', 'description', 'original_type', 'license', 'init_file', 'version', 'parent_elo', 'parent_elo_uuid', 'parent_elo_version']

    def __init__(self, pk=None, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(ELOForkForm, self).__init__(*args, **kwargs)

        elo_original = get_object_or_404(ELO, id=pk)
        elo_source = elo_original

        # If original ELO is not public
        if not elo_original.is_public:
            # and request.user is not author or staff, use Root ELO to replace
            if not self.request_user == elo_original.author or not self.request_user.is_staff:
                elo_source = get_object_or_404(ELO, id=settings.ELO_ROOT_ID)

        self.fields["name"].initial = elo_source.name + " (Fork from author " + elo_source.author.username + ")"
        self.fields["name"].widget.attrs['readonly'] = True
        self.fields["author"].queryset = User.objects.filter(username=self.request_user)
        self.fields["author"].empty_label = None
        self.fields["author"].widget.attrs['readonly'] = True
        self.fields["description"].initial = elo_source.description
        self.fields["description"].widget.attrs['readonly'] = True
        self.fields["original_type"].initial = elo_source.original_type
        self.fields["original_type"].widget.attrs['readonly'] = True
        self.fields["license"].initial = elo_source.license
        self.fields["license"].widget.attrs['readonly'] = True
        self.fields["init_file"].initial = elo_source.init_file
        self.fields["init_file"].widget.attrs['readonly'] = True
        self.fields["version"].initial = 1
        self.fields["version"].widget.attrs['readonly'] = True

        # Even if parent ELO is not public, author and staff still can fork
        if not elo_original.is_public:
            if self.request_user == elo_original.author or self.request_user.is_staff:
                self.fields["parent_elo"].queryset = ELO.objects.filter(id=elo_original.id)
                self.fields["parent_elo_uuid"].initial = elo_original.uuid
                self.fields["parent_elo_version"].initial = elo_original.version
            else:
                self.fields["parent_elo"].queryset = ELO.objects.filter(id=settings.ELO_ROOT_ID)
                self.fields["parent_elo_uuid"].initial = elo_source.uuid
                self.fields["parent_elo_version"].initial = elo_source.version
        # others will force to use Root ELO
        else:
            self.fields["parent_elo"].queryset = ELO.objects.filter(id=settings.ELO_ROOT_ID)
            self.fields["parent_elo_uuid"].initial = elo_source.uuid
            self.fields["parent_elo_version"].initial = elo_source.version

        self.fields["parent_elo"].empty_label = None
        self.fields["parent_elo"].widget.attrs['readonly'] = True
        self.fields["parent_elo_uuid"].widget.attrs['readonly'] = True
        self.fields["parent_elo_version"].widget.attrs['readonly'] = True

        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))

class ELOUpdateForm(ModelForm):
    class Meta:
        model = ELO
        fields = ['name', 'description', 'original_type', 'license', 'metadata', 'is_public', 'init_file']

    def __init__(self, pk=None, *args, **kwargs):
        super(ELOUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = "."
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))
