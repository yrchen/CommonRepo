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
App configurations for ELOs package in Common Repository project.
"""

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig
from actstream import registry


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


class ELOsAppConfig(AppConfig):
    """
    Configs of ELOs packages.
    """
    name = 'commonrepo.elos'

    def ready(self):
        # Register the ELOs package to Activity Stream system
        registry.register(self.get_model('ELO'))
        # Load settings of signals
        import commonrepo.elos.signals
