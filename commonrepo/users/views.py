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

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views.generic.base import TemplateView

from actstream import actions
from actstream.views import respond
from braces.views import LoginRequiredMixin
from notifications.signals import notify

from commonrepo.elos.models import ELO
from commonrepo.groups.models import Group

from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])

        # Count Friends and Followers
        context['has_followed'] = user.userprofile.follows.filter(
            username=self.request.user.username)

        # ELOs
        context['elo_list'] = ELO.objects.filter(author=user).filter(
            is_public=1)[:settings.USERS_MAX_ELOS_PER_PAGE]

        return context


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        # Basic user information
        'id',
        'username',
        'organization',
        'education',
        'url',
        'phone',
        'address',
        'language',
        'area',
        'about',
        # Social informaion
        'social_facebook',
        'social_google',
        'social_linkedin',
        'social_twitter',
        # Extend user information
        'teaching_category',
        'teaching_subject_area',
        # Preferences
        'elo_similarity_threshold']

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
    paginate_by = settings.USERS_MAX_USERS_PER_PAGE


class UserFollowerView(LoginRequiredMixin, ListView):
    template_name = 'users/user_followers.html'
    paginate_by = settings.USERS_MAX_USERS_PER_PAGE

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.followed_by.all()

    def get_context_data(self, **kwargs):
        context = super(UserFollowerView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])

        context['user'] = user

        return context


class UserFollowingView(LoginRequiredMixin, ListView):
    template_name = 'users/user_following.html'
    paginate_by = settings.USERS_MAX_USERS_PER_PAGE

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.userprofile.follows.all()

    def get_context_data(self, **kwargs):
        context = super(UserFollowingView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])

        context['user'] = user

        return context


class UserELOsListView(LoginRequiredMixin, ListView):
    template_name = 'users/user_elos.html'
    paginate_by = settings.USERS_MAX_USERS_PER_PAGE

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])

        # Staff can view all ELOs even it's unpublic
        if self.request.user.is_staff:
            return ELO.objects.filter(author=user)
        else:
            return ELO.objects.filter(author=user).filter(is_public=1)

    def get_context_data(self, **kwargs):
        context = super(UserELOsListView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])

        context['user'] = user

        return context


@login_required
@csrf_exempt
def follow_user(request, username):
    """
    Creates the follow relationship between ``request.user`` and the ``user``
    """
    user = get_object_or_404(User, username=username)

    actions.follow(request.user, user, actor_only=False)
    notify.send(
        request.user,
        recipient=user,
        verb=u'has followed you',
        level='success')
    request.user.userprofile.follows.add(user)
    messages.success(request, 'Successed, you are following this user.')

    return respond(request, 201)   # CREATED


@login_required
@csrf_exempt
def unfollow_user(request, username):
    """
    Deletes the follow relationship between ``request.user`` and the ``user``
    """
    user = get_object_or_404(User, username=username)

    actions.unfollow(request.user, user, send_action=True)
    request.user.userprofile.follows.remove(user)
    messages.warning(
        request,
        'Successed, you are not follow this user anymore.')

    return respond(request, 204)   # NO CONTENT
