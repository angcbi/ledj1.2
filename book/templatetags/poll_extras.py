# -*- coding:utf-8 -*-

import datetime
from django import template

register = template.Library()


def cut(value, arg):
    return value.replace(arg, '')


def lower(value):
    return value.lower()


@register.filter(name='upper')
def upper(value):
    return value.upper()


@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise  template.TemplateSyntaxError
    return CurrentTimeNode(format_string[1:-1])


class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)

list = [
    ('cut', cut),
    ('lower', lower ),
]

for i in list:
    register.filter(i[0], i[1])