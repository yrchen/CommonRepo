# -*- coding: utf-8 -*-

#
# Copyright 2016 edX PDR Lab, National Central University, Taiwan.
#
#     http://edxpdrlab.ncu.cc/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Created By: yrchen@ATCity.org
# Maintained By: yrchen@ATCity.org
#

"""
View configurations for ELOs package in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, ListView, RedirectView, UpdateView, View
from django.shortcuts import redirect, render, get_object_or_404

from actstream import action
from actstream import actions
from actstream.views import respond
from braces.views import LoginRequiredMixin, OrderableListMixin
from notifications.signals import notify
from rest_framework import status

from commonrepo.users.models import User as User

from .models import ELO, ELOMetadata, ELOType, ReusabilityTree, ReusabilityTreeNode
from .forms import ELOForm, ELOForkForm, ELOUpdateForm, ELOMetadataUpdateForm


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class ELOsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View of ``ELO`` creating actions. Render the "ELOs Create" page.

    * Requires authentication.
    """

    model = ELO
    form_class = ELOForm
    template_name = "elos/elos_create.html"
    success_message = "%(name)s was created successfully"

    def get_form_kwargs(self):
        kwargs = super(ELOsCreateView, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def form_valid(self, form):
        # only staff can choose user
        if not self.request.user.is_staff:
            form.instance.author = self.request.user
            form.save()

        return super(ELOsCreateView, self).form_valid(form)

    def get_success_url(self):
        # send action to action stream
        action.send(self.request.user, verb='created', target=self.object)
        return super(ELOsCreateView, self).get_success_url()


class ELOsDetailView(DetailView):
    """
    View of ``ELO`` detail. Render the "ELOs Detail" page.

    * Requires no authentication for basic detail of ELO.
    """

    model = ELO
    query_pk_and_slug = True
    template_name = 'elos/elos_detail.html'

    def dispatch(self, request, *args, **kwargs):
        elo = get_object_or_404(ELO, pk=self.kwargs['pk'])

        # Check the ELO is public or not
        if not elo.is_public:
            if not elo.author == request.user and not request.user.is_staff:
                messages.error(
                    request, 'Permission denied. The target ELO is private.')
                return redirect('elos:elos-alllist')
            else:
                return super(ELOsDetailView, self).dispatch(request,
                                                            *args, **kwargs)
        else:
            return super(ELOsDetailView, self).dispatch(request,
                                                        *args, **kwargs)

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
        context['fork_count'] = ELO.objects.filter(
            parent_elo=self.kwargs['pk']).count()

        return context


class ELOsForkView(LoginRequiredMixin, CreateView):
    """
    View of ``ELO`` forking actions. Render the "ELOs Fork" page.

    * Requires authentication.
    """

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

        # if parent ELO in not public, send a warning message
        if not form.instance.parent_elo.is_public:
            messages.warning(
                self.request,
                'Please be careful, You forked an unpublic ELO!')

        return super(ELOsForkView, self).form_valid(form)

    def get_success_url(self):
        # send action to action stream only when parent ELO is public
        if self.object.parent_elo.is_public:
            action.send(self.request.user, verb='forked', target=self.object)

        return super(ELOsForkView, self).get_success_url()


class ELOsListView(OrderableListMixin, ListView):
    """
    View of ``ELO`` list actions. Render the "All ELOs List" page.

    * Requires authentication.
    """

    template_name = 'elos/elos_list.html'
    paginate_by = settings.ELOS_MAX_ITEMS_PER_PAGE
    orderable_columns = ("id", "create_update", "update_date")
    orderable_columns_default = "id"

    def get_queryset(self):
        """
        Returns the result based on the request.user's permission.
        Only the staff can check all ELOs even it's unpublic.
        """
        if self.request.user.is_staff:
            unordered_queryset = ELO.objects.all()
        else:
            unordered_queryset = ELO.objects.filter(is_public=1)

        # Use get_ordered_queryset from OrderableListMixin
        return self.get_ordered_queryset(unordered_queryset)


class ELOsMyListView(OrderableListMixin, LoginRequiredMixin, ListView):
    """
    View of user related ``ELO`` list actions. Render the "My ELOs List" page.

    * Requires authentication.
    """

    template_name = 'elos/elos_my_list.html'
    paginate_by = settings.ELOS_MAX_ITEMS_PER_PAGE
    orderable_columns = ("id", "create_update", "update_date")
    orderable_columns_default = "id"

    # Use get_ordered_queryset from OrderableListMixin
    def get_queryset(self):
        """
        Returns the result based on the request.user.
        Only list the request.user's own ELOs.
        """
        unordered_queryset = ELO.objects.filter(author=self.request.user)
        return self.get_ordered_queryset(unordered_queryset)


class ELOsFollowingListView(OrderableListMixin, LoginRequiredMixin, ListView):
    """
    View of ``ELO`` following list actions. Render the "ELOs Following List" page.

    * Requires authentication.
    """

    template_name = 'elos/elos_following_list.html'
    paginate_by = settings.ELOS_MAX_ITEMS_PER_PAGE
    orderable_columns = ("id", "create_update", "update_date")
    orderable_columns_default = "id"

    def get_queryset(self):
        """
        Returns the result based on the request.user's following list.
        Only list the public ELOs. Staffs can check all ELOs.
        """
        user = get_object_or_404(User, username=self.request.user.username)

        # Staff can access all ELOs
        if self.request.user.is_staff:
            unordered_queryset = user.userprofile.follow_elos.all()
        else:
            unordered_queryset = user.userprofile.follow_elos.filter(
                is_public=1)

        return self.get_ordered_queryset(unordered_queryset)


class ELOsNetworkView(LoginRequiredMixin, DetailView):
    """
    View of ``ELO`` relation network actions. Render the "ELOs Network" page.

    * Requires authentication.
    """

    model = ELO
    query_pk_and_slug = True
    template_name = 'elos/elos_network.html'

    def dispatch(self, request, *args, **kwargs):
        elo = get_object_or_404(ELO, pk=self.kwargs['pk'])

        # Check the ELO is public or not
        if not elo.is_public:
            if not elo.author == request.user and not request.user.is_staff:
                messages.error(
                    request, 'Permission denied. The target ELO is private.')
                return redirect('elos:elos-alllist')
            else:
                return super(ELOsNetworkView, self).dispatch(request,
                                                             *args, **kwargs)
        else:
            return super(ELOsNetworkView, self).dispatch(request,
                                                         *args, **kwargs)

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
        context['child_elos'] = ELO.objects.filter(
            parent_elo=self.kwargs['pk'])
        return context


class ELOsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View of ``ELO`` updating actions. Render the "ELO Update" page.

    * Requires authentication.
    """

    model = ELO
    form_class = ELOUpdateForm
    query_pk_and_slug = True
    template_name = 'elos/elos_update.html'
    success_message = "%(name)s was updated successfully"

    def dispatch(self, request, *args, **kwargs):
        # Check the request.user has permission to update the specific ELO
        elo = get_object_or_404(ELO, pk=self.kwargs['pk'])

        if not elo.author == request.user and not request.user.is_staff:
            messages.error(request, 'Permission denied.')
            return redirect('elos:elos-alllist')
        else:
            return super(ELOsUpdateView, self).dispatch(request,
                                                        *args, **kwargs)

    def form_valid(self, form):
        # Bumped the version of the related ELO
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


class ELOsMetadataUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View of ``ELO Metadata`` updating actions. Render the "ELO Metadata Update" page.

    * Requires authentication.
    * Requires permission of the specific ``ELO``.
    """

    model = ELOMetadata
    form_class = ELOMetadataUpdateForm
    query_pk_and_slug = False
    template_name = 'elos/elos_metadata_update.html'
    success_message = "The Metadata was updated successfully"

    def dispatch(self, request, *args, **kwargs):
        # Check the request.user has permission to update the specific ELO
        elo = get_object_or_404(ELO, pk=self.kwargs['pk'])

        if not elo.author == request.user and not request.user.is_staff:
            messages.error(request, 'Permission denied.')
            return redirect('elos:elos-alllist')
        else:
            return super(ELOsMetadataUpdateView, self).dispatch(request,
                                                        *args, **kwargs)

    def form_valid(self, form):
        # Bumped the version of the related ELO
        self.object.elo.version += 1
        self.object.elo.save()
        return super(ELOsMetadataUpdateView, self).form_valid(form)

    def get_object(self):
        # Only get the Metadata record from the specific exist ELO
        elo = get_object_or_404(ELO, pk=self.kwargs['pk'])
        return elo.metadata

    def get_form_kwargs(self):
        kwargs = super(ELOsMetadataUpdateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def get_success_url(self):
        # send action to action stream
        action.send(self.request.user, verb='updated', target=self.object.elo)
        return reverse("elos:elos-detail",
                       kwargs={'pk': self.kwargs['pk']})


class ELOTypesDetailView(LoginRequiredMixin, DetailView):
    """
    View of ``ELO`` Type detail actions. Render the "ELO Type Detail" page.

    * Requires authentication.
    """

    model = ELOType
    query_pk_and_slug = True
    template_name = 'elos/elotypes_detail.html'


@login_required
@csrf_exempt
def publish_elo(request, pk):
    """
    Publish the ``ELO``

    * Requires authentication.
    * Requires permission of the specific ``ELO``.
    """
    elo = get_object_or_404(ELO, id=pk)

    # If request.user is author or staff
    if elo.author == request.user or request.user.is_staff:
        elo.is_public = 1
        elo.save()
        action.send(request.user, verb='published', target=elo)
        messages.success(request, 'Successed, the target ELO is public now.')
    else:
        messages.error(request, 'Permission denied.')

    return redirect('elos:elos-detail', pk)


@login_required
@csrf_exempt
def unpublish_elo(request, pk):
    """
    Unpublish the ``ELO``

    * Requires authentication.
    * Requires permission of the specific ``ELO``.
    """
    elo = get_object_or_404(ELO, id=pk)

    # If request.user is author or staff
    if elo.author == request.user or request.user.is_staff:
        elo.is_public = 0
        elo.save()
        messages.warning(request, 'Successed, the target ELO is private now.')
    else:
        messages.error(request, 'Permission denied.')

    return redirect('elos:elos-detail', pk)


@login_required
@csrf_exempt
def follow_elo(request, pk):
    """
    Creates the follow relationship between ``request.user`` and the ``ELO``

    * Requires authentication.
    """
    elo = get_object_or_404(ELO, id=pk)

    if elo.is_public or request.user.is_staff:
        actions.follow(request.user, elo, send_action=True)
        notify.send(
            request.user,
            recipient=elo.author,
            verb=u'has followed your ELO',
            level='success')
        request.user.userprofile.follow_elos.add(elo)
        messages.success(request, 'Successed, you are following this ELO.')
    else:
        messages.error(request, 'Permission denied.')

    return redirect('elos:elos-detail', pk)


@login_required
@csrf_exempt
def unfollow_elo(request, pk):
    """
    Deletes the follow relationship between ``request.user`` and the ``ELO``

    * Requires authentication.
    """
    elo = get_object_or_404(ELO, id=pk)

    actions.unfollow(request.user, elo, send_action=False)
    request.user.userprofile.follow_elos.remove(elo)
    messages.warning(
        request,
        'Successed, you are not follow this ELO anymore.')

    return redirect('elos:elos-detail', pk)
