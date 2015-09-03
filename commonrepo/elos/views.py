# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render

from braces.views import LoginRequiredMixin
from .models import ELO

class MyELOsListView(LoginRequiredMixin, ListView):
    context_object_name = 'myelos_list'
    template_name = 'elos/elos_user_list.html'
    
    def get_queryset(self):
        return ELO.objects.filter(author=self.request.user)    

class MyELOsDetailView(LoginRequiredMixin, DetailView):
    query_pk_and_slug = True
    model = ELO
    template_name = 'elos/elos_detail.html'