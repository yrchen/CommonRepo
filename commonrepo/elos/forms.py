# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.forms import ModelForm
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from commonrepo.users.models import User as User

from .models import ELO

class ELOForm(ModelForm):
    #author = self.request.user.username
    create_date = timezone.now()
    update_date = timezone.now()

    class Meta:
        model = ELO
        fields = ['name', 'author', 'original_type']

    def __init__(self, *args, **kwargs):
        super(ELOForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))

class ELOForkForm(ModelForm):
    class Meta:
        model = ELO
        fields = ['name', 'author', 'original_type']

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(ELOForkForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs['readonly'] = True
        self.fields["author"].queryset = User.objects.filter(username=self.request_user)
        self.fields["author"].empty_label = None
        self.fields["author"].widget.attrs['readonly'] = True
        self.fields["original_type"].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))
