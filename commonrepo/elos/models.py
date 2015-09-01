from django.db import models

# Create your models here.

class ELO(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    original_type = models.SmallIntegerField()
    
    def __unicode__(self):
        return self.name