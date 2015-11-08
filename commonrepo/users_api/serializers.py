# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers

from commonrepo.groups.models import Group as Group
from commonrepo.users.models import User as User

from commonrepo.elos.models import ELO
from commonrepo.snippets_api.models import Snippet

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # ELOs information
    # elos = ForeignKey relationship from model ELO.author
    elos_published = serializers.SerializerMethodField()
    elos_forks = serializers.SerializerMethodField()
    elos_from_others = serializers.SerializerMethodField()

    # Groups
    # commonrepo_groups = ForeignKey relationship from model Group.creator

    # Misc
    # snippets = ForeignKey relationship from model snippets.owner
    
    def get_elos_published(self, obj):
        request = self.context.get("request")
        
        if request and hasattr(request, "user") and request.user.is_authenticated():
            return ELO.objects.filter(author=request.user).filter(is_public=1).count()
        else:
            return -1
    
    def get_elos_forks(self, obj):
        request = self.context.get("request")
        total_forks = 0
        
        if request and hasattr(request, "user") and request.user.is_authenticated():
            my_elo_sets = ELO.objects.filter(author=request.user)
            
            for elo in my_elo_sets:
                total_forks += ELO.objects.filter(parent_elo=elo.id).count()
            
            return total_forks
        
        else:
            return -1
    
    def get_elos_from_others(self, obj):
        request = self.context.get("request")
        
        if request and hasattr(request, "user") and request.user.is_authenticated():
            my_elo_count = ELO.objects.filter(
                    author=request.user).filter(
                    is_public=1).count()
            my_original_elo_count = ELO.objects.filter(
                    author=request.user).filter(
                    is_public=1).filter(
                    parent_elo=1).count()
            return my_elo_count - my_original_elo_count
        
        else:
            return -1

    class Meta:
        model = User
        fields = ('url', 'username', 'organization', 'phone', 'address', 'language', 'area', 'teaching_category', 'teaching_subject_area', 'elos', 'elos_published', 'elos_forks', 'elos_from_others', 'commonrepo_groups', 'snippets', )
