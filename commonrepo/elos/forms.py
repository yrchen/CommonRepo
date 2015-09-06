# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.forms import ModelForm
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

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
