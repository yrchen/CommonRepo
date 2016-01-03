# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, get_object_or_404

from actstream import action
from braces.views import LoginRequiredMixin

from .models import ELO, ELOType, ReusabilityTree, ReusabilityTreeNode
from .forms import ELOForm, ELOForkForm, ELOUpdateForm

class ELOsCreateView(LoginRequiredMixin, CreateView):
    model = ELO
    form_class = ELOForm
    template_name = "elos/elos_create.html"
    #success_url = "/elos"

    def get_success_url(self):
        # send action to action stream
        action.send(self.request.user, verb='created', target=self.object)
        return super(ELOsCreateView, self).get_success_url()


class ELOsDetailView(DetailView):
    model = ELO
    query_pk_and_slug = True
    template_name = 'elos/elos_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ELOsDetailView, self).get_context_data(**kwargs)
        elo = get_object_or_404(ELO, id=self.kwargs['pk'])

        # Check Reusability Tree
        if not hasattr(elo, 'reusability_tree'):
            elo.reusability_tree_build()
        # Force to rebuild every time
        else:
            elo.reusability_tree_update()

        context['nodes'] = ReusabilityTreeNode.objects.filter(base_elo=elo)

        # Count Fork
        context['fork_count'] = ELO.objects.filter(parent_elo=self.kwargs['pk']).count()

        return context

class ELOsForkView(LoginRequiredMixin, CreateView):
    model = ELO
    form_class = ELOForkForm
    template_name = "elos/elos_fork.html"

    def get_form_kwargs(self):
        kwargs = super(ELOsForkView, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def form_valid(self, form):
        # clone metadata
        if form.instance.parent_elo.metadata:
            elo_new_metadata = form.instance.parent_elo.metadata
            elo_new_metadata.pk = None
            elo_new_metadata.save()

            form.instance.metadata = elo_new_metadata
            form.save()

        return super(ELOsForkView, self).form_valid(form)

    def get_success_url(self):
        # send action to action stream
        action.send(self.request.user, verb='forked', target=self.object)
        return super(ELOsForkView, self).get_success_url()

class ELOsListView(LoginRequiredMixin, ListView):
    template_name = 'elos/elos_list.html'

    def get_queryset(self):
        return ELO.objects.all()

class ELOsMyListView(LoginRequiredMixin, ListView):
    template_name = 'elos/elos_my_list.html'

    def get_queryset(self):
        return ELO.objects.filter(author=self.request.user)

class ELOsNetworkView(LoginRequiredMixin, DetailView):
    model = ELO
    query_pk_and_slug = True
    template_name = 'elos/elos_network.html'

    def get_context_data(self, **kwargs):
        context = super(ELOsNetworkView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        elo = get_object_or_404(ELO, id=self.kwargs['pk'])
        parent_elos = []

        if elo.parent_elo_id != settings.ELO_ROOT_ID:
            while elo.parent_elo_id != settings.ELO_ROOT_ID:
                parent_elo = get_object_or_404(ELO, id=elo.parent_elo_id)
                parent_elos.insert(0, parent_elo)
                elo = parent_elo

        context['parent_elos'] = parent_elos
        context['child_elos'] = ELO.objects.filter(parent_elo=self.kwargs['pk'])
        return context

class ELOsUpdateView(LoginRequiredMixin, UpdateView):
    model = ELO
    form_class = ELOUpdateForm
    query_pk_and_slug = True
    template_name = 'elos/elos_update.html'

    def form_valid(self, form):
        self.object.version += 1
        return super(ELOsUpdateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ELOsUpdateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def get_success_url(self):
        # send action to action stream
        action.send(self.request.user, verb='updated', target=self.object)
        return reverse("elos:elos-detail",
                       kwargs={'pk': self.kwargs['pk']})

class ELOTypesDetailView(LoginRequiredMixin, DetailView):
    model = ELOType
    query_pk_and_slug = True
    template_name = 'elos/elotypes_detail.html'
