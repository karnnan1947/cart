from django import template
register=template.Library()
@register.simple_tag(name='multiply')
def number(a,b):
   return a*b