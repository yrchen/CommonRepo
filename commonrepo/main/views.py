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
View configurations for Main app in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from commonrepo.elos.models import ELO
from commonrepo.users.models import User as User


class DashboardView(TemplateView):
    """
    View of dashboard.

    * Requires authentication.
    """

    template_name = 'main/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('home')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        # Common information
        # Only staff can check all ELOs
        if self.request.user.is_staff:
            context['elos_total_count'] = ELO.objects.all().count()
        else:
            context['elos_total_count'] = ELO.objects.filter(
                is_public=1).count()
        context['elos_my_total_count'] = ELO.objects.filter(
            author=self.request.user).count()
        context['users_total_count'] = User.objects.all().count()

        # ELOs
        context['elos_my_list'] = ELO.objects.filter(author=self.request.user).order_by(
            '-update_date')[:settings.DASHBOARD_MAX_ELOS_MY_PER_PAGE]

        # Only staff can check all ELOs
        if self.request.user.is_staff:
            context['elos_all_list'] = ELO.objects.all().order_by(
                '-update_date')[:settings.DASHBOARD_MAX_ELOS_ALL_PER_PAGE]
        else:
            context['elos_all_list'] = ELO.objects.filter(is_public=1).order_by(
                '-update_date')[:settings.DASHBOARD_MAX_ELOS_ALL_PER_PAGE]

        return context
