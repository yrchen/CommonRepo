# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render

from braces.views import LoginRequiredMixin

from .models import Group
from .forms import GroupForm, GroupUpdateForm

class GroupsCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = "groups/groups_create.html"
    #success_url = "/groups"

class GroupsDetailView(LoginRequiredMixin, DetailView):
    model = Group
    query_pk_and_slug = True
    template_name = 'groups/groups_detail.html'

class GroupsListView(LoginRequiredMixin, ListView):
    template_name = 'groups/groups_list.html'

    def get_queryset(self):
        return Group.objects.all()

class GroupsMyListView(LoginRequiredMixin, ListView):
    template_name = 'groups/groups_my_list.html'

    def get_queryset(self):
        return Group.objects.filter(creator=self.request.user)

class GroupsUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupUpdateForm
    query_pk_and_slug = True
    template_name = 'groups/groups_update.html'
    
    def form_valid(self, form):
        self.object.version += 1
        return super(GroupsUpdateView, self).form_valid(form)     

    def get_form_kwargs(self):
        kwargs = super(GroupsUpdateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs
    
    def get_success_url(self):
        return reverse("groups:groups-detail",
                       kwargs={'pk': self.kwargs['pk']})
