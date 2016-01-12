# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from actstream import action
from actstream import registry
from django_comments.signals import comment_was_posted
from threadedcomments.models import ThreadedComment

# Comment has been registeded with actstream.registry.register
def comment_was_posted_handler(sender, comment, request, **kwargs):
    action.send(request.user, verb='posted comment on', action_object=comment, target=comment.content_object)

registry.register(ThreadedComment)
comment_was_posted.connect(comment_was_posted_handler)
