# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.template import TemplateDoesNotExist
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.http import Http404

from .models import Book, Contact


def index(request):
    return render_to_response('book/index.html', {'name': 'django'})


def about_pages(request):
    try:
        return direct_to_template(request, template='about/%s.html' % page)
    except TemplateDoesNotExist:
        raise Http404()


def search(request):
    errors = ''
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors = 'Please Enter Search Words'
        elif len(q)>=20:
            errors = 'Large 20'
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search.html', {'books': books, 'q':q})
    print errors
    return render_to_response('search_form.html',{'errors': errors})

# urlconf 传入字典,获取查询model和template名字
def book_view(request, template_name, model):
    m_list = model.objects.all()
    # template_name = 'book/{}_list.html'.format(model.__name__.lower())
    return render_to_response(template_name, {'m_list':m_list} )


def mydate(request, mouth, day):
    return HttpResponse('2016-{}-{}'.format(mouth, day))


def page(request, num=1):
    return HttpResponse(num)


def method_splitter(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method =='POST' and POST is not None:
        return POST(request)
    else:
        raise Http404

def do_something_get(request):
    assert request.method == 'GET'
    return render_to_response('do_something.html', {'method': request.method})


def do_something_post(request):
    assert request.method == 'POST'
    return render_to_response('do_something.html', {'method': request.method})


# def blog(request, username, page):
#     return HttpResponse('username:{},page:{}'.format(username, page))

def blog(request, username, page=None):
    return HttpResponse('username:{},page:{}'.format(username, page))
