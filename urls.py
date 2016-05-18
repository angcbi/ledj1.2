# coding:utf-8
from django.conf.urls.defaults import *
from mysite1 import views
from django.conf import settings # from mysite1 imort settings
from book import  models as book_models
from book import views as book_views
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from django.contrib.auth.views import login, logout



book_info = {
    'queryset': book_models.Book.objects.all(),  # queryset 在渲染前清理缓存，
    'template_object_name': 'book',
    'extra_context': {'contact_list': book_models.Contact.objects.all}, # 只传到方法，并不调用（没有（）），每次渲染前执行，否则只会在urlconfi加载时执行一次，以后都不执行
}
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# 视图，视图字符串，urlconf字典，url分组，url命名分组，视图函数默认参数
# URLconf是顺序匹配的，找到匹配项就不会继续查找，因此详细匹配规则放前面
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
    (r'^contact_me/$', 'contact.views.contact'),
    (r'^mydate/(?P<mouth>\d{1,2})/((?P<day>\d{1,2}))/$', 'book.views.mydate' ),
    (r'^mydate/birthday/$', 'book.views.mydate', {'mouth': '4', 'day': '2'}),
    # username会传到到include中的每条记录，视图函数没有设置这个参数会报错
    (r'^(?P<username>\w+)/blog/', include('book.urls')),
    (r'^about/$',direct_to_template, {'template': 'about.html'} ),
    (r'^about/(\w+)/$', views.about_pages),
    (r'^bookinfo/$', list_detail.object_list, book_info),
    (r'^bookinfo/(?P<bookname>\w+)/$', book_views.book),
    (r'^downloadtemp', book_views.downloadtemp),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^debug/$', 'views.debug'),
          (r'^accounts/login/$', login, {'template_name': 'login.html'}),
          (r'^accounts/logout/$', logout),
          (r'^accounts/register/$', book_views.register),
    )


urlpatterns += patterns('book.views',
    (r'^search/$', 'search'),
    # 视图函数只关心获取到参数，不关心参数是url捕获的或者是关键字传值来的
    # 如果URLconf捕捉到的一个命名组变量和一个额外URLconf参数包含的变量同名时，额外URLconf参数的值会被使用
    (r'^color/$', 'show_color'),
    (r'^book/$', 'book_view', {'template_name': 'book_list.html', 'model':book_models.Book}),
    (r'^contact/$', 'book_view', {'template_name': 'contact_list.html', 'model':book_models.Contact}),

    # 缺省视图函数参数
    (r'^blog/$', 'page'),
    (r'^blog/page(?P<num>\d+)/$', 'page'),
    # 请求方法
    (r'^somepage/$', 'method_splitter', {'GET':book_views.do_something_get, 'POST':book_views.do_something_post}),
)

