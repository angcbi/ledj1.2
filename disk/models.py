import os
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50,default='')
    email = models.EmailField()
    headimg = models.FileField(upload_to='./upload')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username



