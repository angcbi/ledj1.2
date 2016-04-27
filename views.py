# -*- coding:utf-8 -*-

from datetime import datetime, timedelta
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import loader, RequestContext


def custome_proc(request):
    return {
        'app': 'qq',
        'user': request.user,
        'ip': request.META['REMOTE_ADDR'],
    }


def hello(request):
    # t = loader.get_template('index.html')
    # c = RequestContext(request, {'message': 'cc'}, processors=[custome_proc])
    # return HttpResponse(t.render(c))
    return render_to_response('index.html', {'message':'c 4 345 56 c'}, context_instance=RequestContext(request))

def current_time(request):
    now = datetime.now()
    return HttpResponse(now)


def hours_head(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404

    now = datetime.now()
    hours = now + timedelta(hours=offset)
    return HttpResponse(hours)


def testloop(requests):
    now = datetime.now()
    list = [i for i in range(40)]
    t = Template("""*****
    {{ list|length}}****{{time|date:'Y-m-d H:M:S'}}
    ********
        {% for l in list %}
        第几次循环：{{ forloop.counter }}，当前值为：{{ l }}
        {% if not forloop.last %},{% endif %}
        {% empty %}
        list is empty
        {% endfor %}
    """)
    c = Context({'list': list, 'time': now})
    return HttpResponse(t.render(c))


def debug(request):
    return HttpResponse('debug')