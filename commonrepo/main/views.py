# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from actstream import actions

from commonrepo.elos.models import ELO
from commonrepo.users.models import User as User

class DashboardView(TemplateView):

    template_name='main/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('home')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        # information
        context['elos_total_count'] = ELO.objects.all().count()
        context['elos_my_total_count'] = ELO.objects.filter(author=self.request.user).count()
        context['users_total_count'] = User.objects.all().count()

        # ELOs
        context['elos_my_list'] = ELO.objects.filter(author=self.request.user)[:settings.DASHBOARD_MAX_ELOS_MY_PER_PAGE]
        context['elos_all_list'] = ELO.objects.all()[:settings.DASHBOARD_MAX_ELOS_ALL_PER_PAGE]

        return context

@login_required
@csrf_exempt
def follow_user(request, username):
    """
    Creates or deletes the follow relationship between ``request.user`` and the ``user``
    """
    user = get_object_or_404(User, username=username)

    actions.follow(request.user, user, actor_only=actor_only)
    user.userprofile.follower.add(request.user)

    return respond(request, 201)   # CREATED
