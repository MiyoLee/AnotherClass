from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    return value - int(arg)