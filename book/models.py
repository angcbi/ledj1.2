# -*- coding:utf-8 -*-

import hashlib
from django.db import models


class DahlBookManger(models.Manager):
    def get_query_set(self):
        return super(DahlBookManger, self).get_query_set().filter(title='book10')


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    dahl_objects = DahlBookManger()

    def __unicode__(self):
        return self.title


class Contact(models.Model):
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=100)

    def __unicode__(self):
        return self.subject


class Account(models.Model):
      business_email = models.EmailField()
      business_password = models.CharField(max_length=30)
      contact_first_name = models.CharField(max_length=30)
      contact_last_name = models.CharField(max_length=30)
      is_active = models.BooleanField()

      def is_authenticated(self):
            return True

      def hashed_password(self, password=None):
            if not password:
                  return self.business_password
            else:
                  return hashlib.md5(password).hexdigest()

      def check_password(self, password):
            if self.hashed_password(password) == self.business_password:
                  return True
            return False





