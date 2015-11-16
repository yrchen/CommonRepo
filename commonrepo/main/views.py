# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

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

        context['elos_total_count'] = ELO.objects.all().count()
        context['elos_my_total_count'] = ELO.objects.filter(author=self.request.user).count()
        context['users_total_count'] = User.objects.all().count()
        return context
