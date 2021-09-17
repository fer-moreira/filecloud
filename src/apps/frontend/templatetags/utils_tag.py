from django import template
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

from datetime import datetime, tzinfo
from django.utils.safestring import mark_safe
import timeago

register = template.Library()

@register.filter(name="slugify")
def slugify(value): return slugify(str(value))

@register.simple_tag(name="reverse")
def reverse_url(value): return reverse(value)

@register.simple_tag(name="timeago")
def timeago_date(value): 
    try:
        now = datetime.now().astimezone()
        objdate = value.astimezone()

        time_ago = timeago.format(objdate, now)
        
        return time_ago
    except:
        return "%s/%s/%s" %(value.day, value.month, value.year)

@register.simple_tag(name="sizeof")
def sizeof_fmt(num):
    try:
        assert (type(num) == int), TypeError
        for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
            if abs(num) < 1024.0:
                return "%3.1f %s%s" % (num, unit, 'B')
            num /= 1024.0
        return "%.1f %s%s" % (num, 'Yi', 'B')
    except:
        return num

@register.simple_tag(name="hcontentype")
def hreadable_ctype (value):
    try:
        return value.split("/")[-1]
    except Exception as r:
        print(r)
        return value
