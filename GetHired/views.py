from django.core.exceptions import ObjectDoesNotExist
from django.template import  RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from CSPortal.PostType import model_dict, form_dict
from itertools import chain
from django.core.urlresolvers import reverse
from GetHired import models, forms
import logging
import operator
#main page view

def main(request):
    context = RequestContext(request)
    context_dict = {}
    interview_posts = models.Interview.objects.all()
    offer_posts = models.Offer.objects.all()
    all_posts = sorted(
                       chain(interview_posts,offer_posts),
                       key=lambda post: post.date_posted,
                       reverse = True
                      )
    context_dict['posts'] = all_posts
    context_dict['filters'] = get_filters()
    
    return render_to_response('GetHired/postlist.html', context_dict, context)

def get_filters():

    interview_posts = models.Interview.objects.all()
    offer_posts = models.Offer.objects.all()
    all_posts = sorted(
                       chain(interview_posts,offer_posts),
                       key=lambda post: post.date_posted,
                       reverse = True
                      )
    filters = {}
	
    """The top companies stuff is not used anymore
    top_companies = {}
    #initialize
    for post in all_posts:
        top_companies[post.company.name] = 0

    #count the occurences of each company
    for post in all_posts:
        top_companies[post.company.name] += 1

    sorted_list = sorted(top_companies.iteritems(), 
                         key=operator.itemgetter(1),
                         reverse=True
                         )
    top_companies = []
    limit = 5
    for i in range(0,limit):
        top_companies.append((sorted_list[i])[0])
    """
    filters['companies']= models.Company.objects.all()
    return filters

def get_company_posts(request, company_name):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        #name__iexact is a case-insensitvie match
        company = get_object_or_404(models.Company,name__iexact=company_name)
        #implicit, if company found
        interview_posts = models.Interview.objects.filter(company=company)
        offer_posts = models.Offer.objects.filter(company=company)
        
        all_posts = sorted(
                       chain(interview_posts,offer_posts),
                       key=lambda post: post.date_posted,
                       reverse=True
                      )
        
        context_dict['company'] = company
        context_dict['posts'] = all_posts
        context_dict['filters'] = get_filters()

    return render_to_response('GetHired/postlist.html', context_dict, context)

def get_location_posts(request, company_name):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        #name__iexact is a case-insensitvie match
        company = get_object_or_404(models.Company,name__iexact=company_name)
        #implicit, if company found
        interview_posts = models.Interview.objects.filter(company=company)
        offer_posts = models.Offer.objects.filter(company=company)
        
        all_posts = sorted(
                       chain(interview_posts,offer_posts),
                       key=lambda post: post.date_posted,
                       reverse=True
                      )
        
        context_dict['company'] = company
        context_dict['posts'] = all_posts
        context_dict['filters'] = get_filters()

    return render_to_response('GetHired/postlist.html', context_dict, context)

def get_post(request, post_type, post_id):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        model = model_dict[post_type]
        post = get_object_or_404(model, pk=post_id)
        context_dict['post'] = post

        return render_to_response('GetHired/post.html',context_dict, context)

def render_new_post_form(request,post_type,post_id=None):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        form = form_dict[post_type]
        if post_id:
            Model = model_dict[post_type]
            post = Model.objects.get(pk=post_id)
            context_dict['form'] = form(instance=post)
            context_dict['header'] = 'Edit '
            context_dict['post_id'] = post_id
        else:
            context_dict['form'] = form()
            context_dict['location_form'] = forms.LocationForm()
            context_dict['header'] = 'Add New '
        
        context_dict['post_type'] = post_type
        return render_to_response('portal/newpost.html',context_dict,context)

def render_edit_post_form(request,post_type,post_id):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        form = form_dict[post_type]
        
        if post_id:
            Model = model_dict[post_type]
            post = Model.objects.get(pk=post_id)
            context_dict['form'] = form(instance=post)
            context_dict['header'] = 'Edit '
            context_dict['post_id'] = post_id
        
        context_dict['post_type'] = post_type
        return render_to_response('portal/newpost.html',context_dict,context)


def create_post(request, post_type, post_id=None):
    if request.method == 'POST':
        data = request.POST
        logging.debug(request.POST)
        Form = form_dict[post_type]
        context = RequestContext(request)
        context_dict = {}
        user_form = Form(request.POST)
        l = None
        if user_form.is_valid():
            if ('country' in data) and ('state' in data) and ('city' in data):
                l = models.Location(country=data['country'],state=data['state'],city=data['city'])
                l.save()
            else:
                pass #some error

            logging.debug(l)
            if post_id:
                model = model_dict[post_type]
                post = model.objects.get(pk=post_id)
                user_form = Form(request.POST, instance=post) 
            
            post = user_form.save()
            post.location = l
            post.save()
            #return render_to_response('portal/newpost.html',context_dict, context)
            return HttpResponseRedirect('/gethired/')
        else:
            context_dict['form'] = user_form
            logging.debug(user_form)
            context_dict['post_type'] = post_type
            return render_to_response('portal/newpost.html',context_dict, context)

"""def edit_post(request, post_type, post_id=None):
    if request.method == 'POST':
        Form = form_dict[post_type]
        context = RequestContext(request)
        context_dict = {}
        if user_form.is_valid():
            model = model_dict[post_type]
            post = model.objects.get(pk=post_id)
            user_form = Form(request.POST, instance=post)

            user_form.save()
            return HttpResponseRedirect('/GetHired/')
        else:
            context_dict['form'] = user_form
            context_dict['post_type'] = post_type
            return render_to_response('portal/newpost.html',context_dict, context)
"""

def filter_posts(request):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        data = request.GET
        
        filters = {}
        
        if 'post_type' in data:
            models_requested = data.getlist('post_type')    
        else:
            models_requested = ['Interview','Offer']

        if 'location' in data and data['location'] != 'ALL':
            filters['location__state'] = data['location']

        if 'job_type' in data and data['job_type'] != 'ALL':
            filters['job_type'] = data['job_type']
        
        if 'job_title' in data and data['job_title'] != 'ALL': 
            filters['job_title']= data['job_title']

        if 'company' in data and data['company'] != 'ALL': 
            filters['company__name']= data['company']

        all_posts = []
        
        for m in models_requested:
            Model = model_dict[m]
            posts = Model.objects.filter(**filters)
            all_posts.extend(posts)

        all_posts.sort(key=lambda post: post.date_posted,reverse=True)
        context_dict['posts'] = all_posts
        context_dict['filters'] = get_filters()
        return render_to_response('GetHired/postlist.html',context_dict,context)
     
