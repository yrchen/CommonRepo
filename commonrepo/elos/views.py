# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render

from braces.views import LoginRequiredMixin

from .models import ELO
from .forms import ELOForm, ELOForkForm

class ELOsCreateView(LoginRequiredMixin, CreateView):
    model = ELO
    form_class = ELOForm
    template_name = "elos/elos_create.html"
    #success_url = "/elos"

class ELOsForkView(LoginRequiredMixin, CreateView):
    model = ELO
    form_class = ELOForkForm
    template_name = "elos/elos_fork.html"
    
    def get_form_kwargs(self):
        kwargs = super(ELOsForkView, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs    

class ELOsListView(LoginRequiredMixin, ListView):
    template_name = 'elos/elos_list.html'

    def get_queryset(self):
        return ELO.objects.all()

class MyELOsListView(LoginRequiredMixin, ListView):
    template_name = 'elos/elos_my_list.html'

    def get_queryset(self):
        return ELO.objects.filter(author=self.request.user)

class MyELOsDetailView(LoginRequiredMixin, DetailView):
    query_pk_and_slug = True
    model = ELO
    template_name = 'elos/elos_detail.html'
