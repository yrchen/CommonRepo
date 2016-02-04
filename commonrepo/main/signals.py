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
Signal configurations for Main app in Common Repository project.

The following common functions will been handled in the Main app:
* comments (ThreadedComment)
"""

from __future__ import absolute_import, unicode_literals

from actstream import action
from actstream import registry
from django_comments.signals import comment_was_posted
from threadedcomments.models import ThreadedComment

# Comment has been registeded with actstream.registry.register


__author__ = 'yrchen@ATCity.org (Xaver Y.R. Chen)'


# Handler of comment posted actions
def comment_was_posted_handler(sender, comment, request, **kwargs):
    action.send(
        request.user,
        verb='posted comment',
        action_object=comment,
        target=comment.content_object)

registry.register(ThreadedComment)

# Registered the handlers of Comments to Activity Streams.
comment_was_posted.connect(comment_was_posted_handler)
