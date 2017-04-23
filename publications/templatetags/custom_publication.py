
from django import template
register = template.Library()

@register.filter(is_safe=True)
def custom_datatime(value):
    return value.strftime("%m-%d-%Y")
