# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^page/$', 'book.views.page'),
    # (r'^(?P<page>\d+)/$', 'book.views.page'),
)