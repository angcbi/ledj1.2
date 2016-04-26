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


def search_form(requests):
    return render_to_response('search_form.html')


def search(requests):
    if 'q' in requests.GET and requests.GET['q']:
        q = requests.GET['q']
        books = Book.objects.filter(title__icontains=q)
        print len(books)
        return render_to_response('search.html', {'books': books, 'q':q})
    else:
        return render_to_response('search_form.html',{'error': True})
