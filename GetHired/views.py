from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import  RequestContext
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q
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

    paginator = Paginator(all_posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context_dict['posts'] = posts
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

def get_field_posts(request, field_name, field_value):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        #name__iexact is a case-insensitvie match

        if (field_name == "company"):
            field_value = field_value.replace('-', ' ')
            company = get_object_or_404(models.Company, name__iexact=field_value)
            interview_posts = models.Interview.objects.filter(company=company)
            offer_posts = models.Offer.objects.filter(company=company)
            context_dict['company'] = company

        elif (field_name == "location"):
            if (field_value == "International"):
                interview_posts = models.Interview.objects.exclude(location__country="US")
                offer_posts = models.Offer.objects.exclude(location__country="US")

            else:
                interview_posts = models.Interview.objects.filter(location__state=field_value)
                offer_posts = models.Offer.objects.filter(location__state=field_value)

            
        
        all_posts = sorted(
                       chain(interview_posts,offer_posts),
                       key=lambda post: post.date_posted,
                       reverse=True
                       )

        paginator = Paginator(all_posts, 10)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)                  
        
        context_dict['posts'] = posts
        context_dict['filters'] = get_filters()

    return render_to_response('GetHired/postlist.html', context_dict, context)

def get_related_posts(post_type, post_id):
    Model = model_dict[post_type]
    post = Model.objects.get(pk=post_id)
    #See if there are any posts that match all relevant criteria
    candidates_posts = Model.objects.exclude(id=post_id)
    relevance = []

    for i in range(len(candidates_posts)):
        p = candidates_posts[i]
        points = 0

        if p.company == post.company: points+=1
        if p.location == post.location: points+=1 
        if p.job_type == post.job_type: points+=1 

        relevance.append((i,points))

    #find more relevant ones and put them up front    
    relevance.sort(key=lambda tup: tup[1], reverse=True)
    #get the indexes of the top posts and retrieve them
    logging.debug(relevance)
    relevant_posts = []
    for r in relevance[:5]:
        index = r[0]
        if r[1] > 0:
            relevant_posts.append(candidates_posts[index])

    return relevant_posts




def get_post(request, post_type, post_id):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        post_type = post_type.capitalize()
        model = model_dict[post_type]
        post = get_object_or_404(model, pk=post_id)
        context_dict['post'] = post
        context_dict['related_posts'] = get_related_posts(post_type, post_id)

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
            context_dict['location_form'] = forms.LocationForm(instance=post.location)

            context_dict['header'] = 'Edit '
            context_dict['post_id'] = post_id
        else:
            context_dict['form'] = form()
            context_dict['location_form'] = forms.LocationForm()
            context_dict['header'] = 'Add New '
        
        context_dict['post_type'] = post_type
        return render_to_response('portal/newpost.html',context_dict,context)
"""
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
"""

def create_post(request, post_type, post_id=None):
    if request.method == 'POST':
        data = request.POST
        Form = form_dict[post_type]
        context = RequestContext(request)
        context_dict = {}
        user_form = Form(request.POST)
        location = None

        if user_form.is_valid():
            if ('country' in data) and ('state' in data) and ('city' in data):
                location = models.Location(country=data['country'],state=data['state'],city=data['city'])
                location.save()
            else:
                pass #some error

            if post_id:
                model = model_dict[post_type]
                post = model.objects.get(pk=post_id)
                user_form = Form(request.POST, instance=post) 
            
            post = user_form.save()
            post.location = location
            post.save()
            #return render_to_response('portal/newpost.html',context_dict, context)
            return HttpResponseRedirect('/gethired/')
        else:
            context_dict['form'] = user_form
            context_dict['location_form'] = forms.LocationForm({'country':data['country'],'state':data['state'],'city':data['city']})
            logging.debug(context_dict['location_form'])
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

        paginator = Paginator(all_posts, 10)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context_dict['posts'] = posts
        context_dict['filters'] = get_filters()
        return render_to_response('GetHired/postlist.html',context_dict,context)
     
