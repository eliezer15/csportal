from django import template

register = template.Library()

@register.filter
def class_name(obj):
    classname= obj.__class__.__name__
    return classname
