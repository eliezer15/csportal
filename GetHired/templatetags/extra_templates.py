import urlparse
from django import template
from django.template.defaulttags import URLNode, url
from django.contrib.sites.models import Site

register = template.Library()

@register.filter
def classname(obj):
    classname= obj.__class__.__name__
    return classname

@register.filter
def normdegree(value):
    degree_choices = {
            'MI':'Minor',
            'BA': 'Bachelor of Arts',
            'BS': 'Bachelor of Science',
            'MA': 'Master of Arts',
            'MS': 'Master of Science',
            'MB': 'MBA',
            'PD': 'Ph.D',
            'PR': 'Professional Degree',
            'OT': 'Other'}
    return degree_choices[value]

@register.filter
def tagline(value):
    return value[:140] + '...'

@register.filter
def normcompname(value):
    return value.replace(' ', '%20')
	
class AbsoluteURLNode(URLNode):
    def render(self, context):
        path = super(AbsoluteURLNode, self).render(context)
        domain = "http://%s" % Site.objects.get_current().domain
        return urlparse.urljoin(domain, path)

def absurl(parser, token, node_cls=AbsoluteURLNode):
    """Just like {% url %} but ads the domain of the current site."""
    node_instance = url(parser, token)
    return node_cls(view_name=node_instance.view_name,
        args=node_instance.args,
        kwargs=node_instance.kwargs,
        asvar=node_instance.asvar)

absurl = register.tag(absurl)
