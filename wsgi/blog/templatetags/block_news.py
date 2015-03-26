'''
Created on Oct 19, 2014
@author: hide
'''
from django import template
register = template.Library()
from blog.models import Page
@register.inclusion_tag('news.html')
def show_news( *args, **kwargs):
    pass
    pages = Page.objects.all().order_by('pub_date')
    return {'data': pages}


