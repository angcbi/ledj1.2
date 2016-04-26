# coding:utf-8
from django.conf.urls.defaults import *
from views import hello, current_time, hours_head, testloop
from django.contrib import admin
# from django.views.generic.simple import  direct_to_template
# from book.views import about_pages


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite1/', include('mysite1.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # (r'^disk/$', 'disk.views.register'),
    # (r'^cookie/$', 'disk.views.cook'),
    # (r'^login/$', 'disk.views.login'),
    (r'^$', hello),
    (r'^time/$', current_time),
    (r'^time/plus/(\d{1,2})/$', hours_head),
    (r'^testloop/$', testloop),
    (r'^search-form/$', 'book.views.search_form'),
    (r'^search/$', 'book.views.search'),
)
