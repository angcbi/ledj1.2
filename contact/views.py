# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from contact.forms import ContactForm
from book.models import Contact
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                Contact.objects.create(**cd)
                return HttpResponse('add success')
            except Exception, e:
                return HttpResponse('fail')
    else:
        form = ContactForm(initial={'subject': '', 'email':'' ,'message':''})

    return render_to_response('contact.html', {'form': form})





