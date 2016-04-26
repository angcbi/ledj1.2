# -*- coding:utf-8 -*-

from datetime import datetime, timedelta
from django.http import HttpResponse, Http404
from django.template import Template, Context


def hello(request):
    return HttpResponse('hello')


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
    list = []
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

