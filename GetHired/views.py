from GetHired.models import Interview, Offer
from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from CSPortal.PostType import model_dict, form_dict
from itertools import chain
from django.core.urlresolvers import reverse

#main page view

def main(request):
    context = RequestContext(request)
    context_dict = {}
    interview_posts = []
    offer_posts = []

    try:
        interview_posts = Interview.objects.all()
    except Interview.DoesNotExist:
        pass

    try:
        offer_posts = Offer.objects.all()
    except Offer.DoesNotExist:
        pass

    all_posts = sorted(
                       chain(interview_posts,offer_posts),
                       key=lambda post: post.date_posted
                      )

    all_posts.reverse() #sort decreasing date
    context_dict['posts'] = all_posts

    return render_to_response('GetHired/postlist.html', context_dict, context)

def get_post(request, post_type, post_id):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        model = model_dict[post_type]
        post = model.objects.get(pk=post_id)
        context_dict['post'] = post

        return render_to_response('GetHired/post.html',context_dict, context)

def new_post(request,post_type):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        form = form_dict[post_type]
        context_dict['form'] = form
        context_dict['post_type'] = post_type

        return render_to_response('portal/newpost.html',context_dict,context)
def create_post(request, post_type):
    if request.method == 'POST':
        Form = form_dict[post_type]
        context = RequestContext(request)
        context_dict = {}
        user_form = Form(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/GetHired/')
        else:
            context_dict['form'] = user_form
            context_dict['post_type'] = post_type
            return render_to_response('portal/newpost.html',context_dict, context)


