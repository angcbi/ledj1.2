# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.http import Http404
from django.template import RequestContext
from django.views.generic import list_detail
from django import forms
from django.contrib.auth.forms import UserCreationForm
import json

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
    return render_to_response(template_name, {'m_list':m_list}, context_instance=RequestContext(request) )


def mydate(request, mouth, day):
    return HttpResponse('2016-{}-{}'.format(mouth, day))


def page(request, num=1):
      print 'META', request.META['User-Agent']
      print '*'*20
      print 'REQUEST',request.REQUEST.items()
      print '*'*20
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

def blog(request, username, page):
    return HttpResponse('username:{},page:{}'.format(username, page))


def book(request, bookname):
    return list_detail.object_list(
        request,
        queryset = Book.objects.filter(title__icontains=bookname),
        template_object_name= 'book'
    )


def show_color(request):
      if 'color' in request.GET:
            color = request.GET['color']
            response = HttpResponse('color is %s ' % color)
            response.set_cookie('color',color, max_age=60*60*12)
            request.session['color'] = '123124'
            return  response
      return HttpResponse('you have no color')


def register(request):
      if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  new_user = form.save()
                  return HttpResponseRedirect('/time')
      else:
            form = UserCreationForm()

      return render_to_response('register.html', {'form': form})


def downloadtemp(request):
      res = {'success': False, 'data': {}, 'message': ''}
      response = HttpResponse(mimetype='application/vnd.ms-excel')
      with open(r'e:\355420_employee.xls', 'rb') as f:
            res['data'] = f.read()
            response.write(res)
            response['Content-Disposition'] =  'attachment; filename=unruly.xls'

      return response

