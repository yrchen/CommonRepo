# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from actstream import actions
from actstream.views import respond

from braces.views import LoginRequiredMixin

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
        context['has_followed'] = user.userprofile.follows.filter(username=self.request.user.username)

        # ELOs
        context['elo_list'] = ELO.objects.filter(author=user).filter(is_public=1)

        return context


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        # Basic user information
        'id', 'username', 'organization', 'education', 'url', 'phone', 'address', 'language', 'area', 'about',
        # Social informaion
        'social_facebook', 'social_google', 'social_linkedin', 'social_twitter',
        # Extend user information
        'teaching_category', 'teaching_subject_area',
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

@login_required
@csrf_exempt
def follow_user(request, username):
    """
    Creates the follow relationship between ``request.user`` and the ``user``
    """
    user = get_object_or_404(User, username=username)

    actions.follow(request.user, user, actor_only=False)
    request.user.userprofile.follows.add(user)

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

    return respond(request, 204)   # NO CONTENT