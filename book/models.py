# -*- coding:utf-8 -*-

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

