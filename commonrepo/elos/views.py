# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render

from braces.views import LoginRequiredMixin

from .models import ELO
from .forms import ELOForm, ELOForkForm, ELOUpdateForm

class ELOsCreateView(LoginRequiredMixin, CreateView):
    model = ELO
    form_class = ELOForm
    template_name = "elos/elos_create.html"
    #success_url = "/elos"

class ELOsDetailView(LoginRequiredMixin, DetailView):
    model = ELO
    query_pk_and_slug = True
    template_name = 'elos/elos_detail.html'


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

class ELOsMyListView(LoginRequiredMixin, ListView):
    template_name = 'elos/elos_my_list.html'

    def get_queryset(self):
        return ELO.objects.filter(author=self.request.user)

class ELOsUpdateView(LoginRequiredMixin, UpdateView):
    model = ELO
    form_class = ELOUpdateForm
    query_pk_and_slug = True
    template_name = 'elos/elos_update.html'

    def get_success_url(self):
        return reverse("elos:elos-detail",
                       kwargs={'pk': self.kwargs['pk']})
