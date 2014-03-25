'''
Created on Mar 18, 2014

@author: encarnae
'''
from CSPortal.PostType import model_dict
from django.utils import simplejson
from GetHired.models import Interview
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from dajax.core import Dajax

'''view_post creates the expanded view of a specific post'''
@dajaxice_register(method='GET', name='post.get')
def view_post(request, post_id, post_type):
    context_dict = {}
    if (request.method == 'GET'):
        if post_id:
            model = model_dict[post_type]
            post = model.objects.get(pk=post_id)
            context_dict['post'] = post
            render = render_to_string('GetHired/post.html', context_dict)
            return simplejson.dumps({'post': render})

