from django import template
register=template.Library()
@register.simple_tag(name='status')
def number(statu):
   statu-=1
   status_array=['confirmed','processed','delivered','rejected']
   return status_array[statu]