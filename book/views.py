# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.template import TemplateDoesNotExist
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.http import Http404

from book.models import Book

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
