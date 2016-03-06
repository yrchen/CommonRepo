# -*- coding: utf-8 -*-

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
Common router API for Common Repository project.

This is a replace version of DefaultRouter from Django REST Framework.
https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/routers.py

Routers provide a convenient and consistent way of automatically
determining the URL conf for your API.
They are used by simply instantiating a Router class, and then registering
all the required ViewSets with that router.
For example, you might have a `urls.py` that looks something like this:
    router = routers.DefaultRouter()
    router.register('users', UserViewSet, 'user')
    router.register('accounts', AccountViewSet, 'account')
    urlpatterns = router.urls
"""
from __future__ import unicode_literals

from django.conf.urls import url

from rest_framework.routers import DefaultRouter as RESTDefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class DefaultRouter(RESTDefaultRouter):
    root_view_name = 'api-root'
    root_view_prefix = 'api' + '^$'

    def get_urls(self):
        """
        Generate the list of URL patterns, including a default root view
        for the API, and appending `.json` style format suffixes.
        """
        urls = []

        if self.include_root_view:
            root_url = url(r'^api/$',
                           self.get_api_root_view(),
                           name=self.root_view_name)
            urls.append(root_url)

        default_urls = super(RESTDefaultRouter, self).get_urls()
        urls.extend(default_urls)

        if self.include_format_suffixes:
            urls = format_suffix_patterns(urls)

        return urls
