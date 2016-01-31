# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from haystack import indexes

from .models import ELO


class ELOIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    create_date = indexes.DateTimeField(model_attr='create_date')
    update_date = indexes.DateTimeField(model_attr='update_date')

    def get_model(self):
        return ELO
