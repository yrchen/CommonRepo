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
View configurations for Groups in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import redirect, get_object_or_404

from actstream import action
from actstream import actions
from braces.views import LoginRequiredMixin, OrderableListMixin
from notifications.signals import notify

from commonrepo.users.models import User as User

from .models import Group
from .forms import GroupForm, GroupUpdateForm, GroupAddForm, GroupLeaveForm


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class GroupsAbortView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View of group aborting actions.

    * Requires authentication.
    """

    model = Group
    form_class = GroupLeaveForm
    query_pk_and_slug = True
    template_name = 'groups/groups_abort.html'
    success_message = "You aborted Group %(name)s successfully"

    def form_valid(self, form):
        # remove request user from the members of group
        form.instance.members.remove(self.request.user)
        form.save()

        return super(GroupsAbortView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(GroupsAbortView, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def get_success_url(self):
        action.send(self.request.user, verb='aborted', target=self.object)
        actions.unfollow(self.request.user, self.object, send_action=False)
        notify.send(
            self.request.user,
            recipient=self.object.creator,
            verb=u'has aborted from your Group',
            level='success')
        return reverse("groups:groups-detail",
                       kwargs={'pk': self.kwargs['pk']})


class GroupsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View of group creating actions.

    * Requires authentication.
    """

    model = Group
    form_class = GroupForm
    template_name = "groups/groups_create.html"
    success_message = "%(name)s was created successfully"

    def get_form_kwargs(self):
        kwargs = super(GroupsCreateView, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def get_success_url(self):
        action.send(self.request.user, verb='created', target=self.object)
        return super(GroupsCreateView, self).get_success_url()


class GroupsDetailView(LoginRequiredMixin, DetailView):
    """
    View of group details.

    * Requires authentication.
    """

    model = Group
    query_pk_and_slug = True
    template_name = 'groups/groups_detail.html'


class GroupsJoinView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View of group joining actions.

    * Requires authentication.
    """

    model = Group
    form_class = GroupAddForm
    query_pk_and_slug = True
    template_name = 'groups/groups_join.html'
    success_message = "You joined Group %(name)s successfully"

    def form_valid(self, form):
        # add request user to the members of group
        form.instance.members.add(self.request.user)
        form.save()

        return super(GroupsJoinView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(GroupsJoinView, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def get_success_url(self):
        action.send(self.request.user, verb='joined', target=self.object)
        actions.follow(self.request.user, self.object, send_action=True)
        notify.send(
            self.request.user,
            recipient=self.object.creator,
            verb=u'has joined to your Group',
            level='success')
        return reverse("groups:groups-detail",
                       kwargs={'pk': self.kwargs['pk']})


class GroupsListView(LoginRequiredMixin, ListView):
    """
    View of group list actions.

    * Requires authentication.
    """

    template_name = 'groups/groups_list.html'
    paginate_by = settings.GROUPS_MAX_ITEMS_PER_PAGE

    def get_queryset(self):
        return Group.objects.all()


class GroupsMyListView(LoginRequiredMixin, ListView):
    """
    View of user related group list actions.

    * Requires authentication.
    """

    template_name = 'groups/groups_my_list.html'
    paginate_by = settings.GROUPS_MAX_ITEMS_PER_PAGE

    def get_queryset(self):
        return Group.objects.filter(creator=self.request.user)


class GroupsFollowingListView(
        OrderableListMixin,
        LoginRequiredMixin,
        ListView):
    """
    View of group following list actions.

    * Requires authentication.
    """

    template_name = 'groups/groups_following_list.html'
    paginate_by = settings.GROUPS_MAX_ITEMS_PER_PAGE
    orderable_columns = ("id", "create_update", "update_date")
    orderable_columns_default = "id"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        unordered_queryset = user.userprofile.follow_groups.all()

        return self.get_ordered_queryset(unordered_queryset)


class GroupsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View of group updating actions.

    * Requires authentication.
    """

    model = Group
    form_class = GroupUpdateForm
    query_pk_and_slug = True
    template_name = 'groups/groups_update.html'
    success_message = "%(name)s was updated successfully"

    def dispatch(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])

        if not group.creator == request.user and not request.user.is_staff:
            messages.error(request, 'Permission denied.')
            return redirect('groups:groups-alllist')
        else:
            return super(
                GroupsUpdateView,
                self).dispatch(
                request,
                *
                args,
                **kwargs)

    def form_valid(self, form):
        #    self.object.version += 1
        return super(GroupsUpdateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(GroupsUpdateView, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def get_success_url(self):
        action.send(self.request.user, verb='updated', target=self.object)
        return reverse("groups:groups-detail",
                       kwargs={'pk': self.kwargs['pk']})


@login_required
@csrf_exempt
def follow_group(request, pk):
    """
    Creates the follow relationship between ``request.user`` and the ``Group``
    """
    group = get_object_or_404(Group, id=pk)

    # Check user is not member of the group
    if not group.members.filter(id=request.user.id).exists():
        actions.follow(request.user, group, send_action=True)
        notify.send(
            request.user,
            recipient=group.creator,
            verb=u'has followed your Group',
            level='success')
        request.user.userprofile.follow_groups.add(group)
        messages.success(
            request,
            'Successed, you are now following this Group.')
    else:
        actions.follow(request.user, group, send_action=False)
        messages.success(
            request,
            'You are the member of this Group and automatically become the follower.')

    return redirect('groups:groups-detail', pk)


@login_required
@csrf_exempt
def unfollow_group(request, pk):
    """
    Deletes the follow relationship between ``request.user`` and the ``Group``
    """
    group = get_object_or_404(Group, id=pk)

    # Check user is not member of the group
    if not group.members.filter(id=request.user.id).exists():
        actions.unfollow(request.user, group, send_action=False)
        request.user.userprofile.follow_groups.remove(group)
        messages.warning(
            request,
            'Successed, you are not following this Group anymore.')
    # the group members can choose not follow the group anymore, but still
    # been the member
    else:
        actions.unfollow(request.user, group, send_action=False)
        messages.warning(
            request,
            'Successed, you are not following this Group anymore. But you are still the one of the members of this group.')

    return redirect('groups:groups-detail', pk)
