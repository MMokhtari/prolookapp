from django.db import models
from datetime import datetime
class Visitor(models.Model):
    user_agent = models.CharField(max_length=250,blank=False) 
    ip = models.CharField(max_length=30, blank=False)
    refer = models.CharField(max_length=80, default='None')
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.ip