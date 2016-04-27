# coding:utf-8
from django.conf.urls.defaults import *
from mysite1 import views
from django.conf import settings # from mysite1 imort settings
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
    # (r'^admin/', include(admin.site.urls)),
    # (r'^disk/$', 'disk.views.register'),
    # (r'^cookie/$', 'disk.views.cook'),
    # (r'^login/$', 'disk.views.login'),
    (r'^$', views.hello),
    (r'^time/$', views.current_time),
    # 命名组和非命名组是不能同时存在于同一个URLconf,有命名组，会忽略非命名组
    (r'^time/plus/(?P<offset>\d{1,2})/$', views.hours_head),
    (r'^testloop/$', views.testloop),
    (r'^contact/$', 'contact.views.contact'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^debug/$', 'views.debug'),
    )

urlpatterns += patterns('book.views',
    (r'^search/$', 'search'),
)

