# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render

from braces.views import LoginRequiredMixin

from .models import ELO
from .forms import ELOForm

class MyELOsCreateView(LoginRequiredMixin, CreateView):
    model = ELO
    form_class = ELOForm
    template_name = "elos/elos_create.html"
    #success_url = "/elos"

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
