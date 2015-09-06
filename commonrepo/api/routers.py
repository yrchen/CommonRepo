# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from rest_framework.routers import DefaultRouter as RESTDefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

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
            root_url = url(r'^api/$', self.get_api_root_view(), name=self.root_view_name)
            urls.append(root_url)
    
        default_urls = super(RESTDefaultRouter, self).get_urls()
        urls.extend(default_urls)
    
        if self.include_format_suffixes:
            urls = format_suffix_patterns(urls)
    
        return urls    