from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import  RequestContext
from django.shortcuts import render_to_response,get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from CSPortal.PostType import model_dict, form_dict
from itertools import chain
from GetHired import models, forms
from django.forms.util import ErrorList
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from registration.backends.default.views import RegistrationView
from django.core.mail import EmailMessage
from django.http import Http404
from bs4 import BeautifulSoup
from django.contrib import messages
import random
import logging
import simplejson
import hashlib




def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('portal/index.html', context_dict, context)

def main(request, site):

    context = RequestContext(request)
    context_dict = {}

    if site == "gethired":
        interview_posts = models.Interview.objects.all()
        offer_posts = models.Offer.objects.all()
        all_posts = sorted(
                           chain(interview_posts,offer_posts),
                           key=lambda post: post.date_posted,
                           reverse = True
                          )
    elif site == "marketplace":
        all_posts = models.Project.objects.order_by('date_posted').reverse()

    elif site == "jobs":
        all_posts = models.Job.objects.order_by('date_posted').reverse()

    paginator = Paginator(all_posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context_dict['posts'] = posts
    
    if (site == 'gethired'):
        context_dict['filters'] = get_filters_gethired()
    if (site == 'marketplace'):
        context_dict['filters'] = get_filters_marketplace()
    if (site == 'gethired'):
        context_dict['filters'] = get_filters_gethired()
    
    return render_to_response(site+'/postlist.html', context_dict, context)

def get_filters_gethired():
    filters = {}

    filters['companies']= models.Company.objects.order_by('name')
    return filters

def get_filters_marketplace():
    filters = {}

    filters['technologies']= models.Technology.objects.order_by('name')
    return filters

@login_required
def get_company(request, name):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        name = name.replace('-', ' ')
        company = get_object_or_404(models.Company, name__iexact=name)
        interview_posts = models.Interview.objects.filter(company=company)
        offer_posts = models.Offer.objects.filter(company=company)
        context_dict['company'] = company
        
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
        context_dict['filters'] = get_filters_gethired()

        return render_to_response('gethired/postlist.html', context_dict, context)

def get_related_posts_gethired(post_type, post_id):
    Model = model_dict[post_type]
    post = Model.objects.get(pk=post_id)
    #See if there are any posts that match all relevant criteria
    candidates_posts = Model.objects.exclude(id=post_id, deleted=True)
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

@login_required
def get_post_gethired(request, post_type, post_id):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        model = model_dict[post_type]
        post = get_object_or_404(model, pk=post_id)
        if post.deleted:
            raise Http404

        context_dict['post'] = post
        context_dict['related_posts'] = get_related_posts_gethired(post_type, post_id)

        return render_to_response('gethired/post.html',context_dict, context)

def get_post_job(request, post_id):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        post = get_object_or_404(models.Job, pk=post_id)
        if post.deleted:
            raise Http404

        context_dict['post'] = post
        context_dict['related_posts'] = get_related_posts_job(post_id)

        return render_to_response('jobs/post.html',context_dict, context)


def get_related_posts_job(post_id):
    post = models.Job.objects.get(pk=post_id)
    candidates_posts = models.Job.objects.exclude(pk=post_id, deleted=True)
    relevance = []

    for i in range(len(candidates_posts)):
        p = candidates_posts[i]
        points = 0

        if p.company == post.company: points+=1
        if p.location == post.location: points+=1 
        if p.job_type == post.job_type: points+=1 
        t1 = set(p.technologies.all())
        t2 = set(post.technologies.all())
        intersection = t1 & t2

        points += len(intersection)

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

@login_required
def render_new_post_form(request, post_type,post_id=None):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        form = form_dict[post_type]

        context_dict['companies'] = models.Company.objects.order_by('name');

        if post_id:
            Model = model_dict[post_type]
            post = get_object_or_404(Model, pk=post_id)
            modelform = form(instance=post)
            if post_type == "interview":
                modelform.fields['offer_details'].queryset = models.Offer.objects.filter(author = request.user)
            context_dict['form'] = modelform
            context_dict['location_form'] = forms.LocationForm(instance=post.location)
            context_dict['company_form'] = forms.CompanyForm(instance=post.company)
            context['author'] = post.author
            
            context_dict['header'] = 'Edit '
            context_dict['post_id'] = post_id
        else:
            modelform = form()
            if post_type == "interview":
                modelform.fields['offer_details'].queryset = models.Offer.objects.filter(author = request.user)
            context_dict['form'] = modelform
            context_dict['location_form'] = forms.LocationForm()
            context_dict['company_form'] = forms.CompanyForm()
            context_dict['header'] = 'Add New '
        
        context_dict['post_type'] = post_type
        if post_type == "project":
            return render_to_response('marketplace/newpost.html', context_dict, context)
        return render_to_response('gethired/newpost.html',context_dict,context)


def create_post_gethired(request, post_type, post_id=None):
    if request.method == 'POST':
        data = request.POST
        Form = form_dict[post_type]
        context = RequestContext(request)
        context_dict = {}
        if post_id:
                model = model_dict[post_type]
                post = model.objects.get(pk=post_id)
                user_form = Form(request.POST, instance=post) 
        else:
            user_form = Form(request.POST)
        location = None
        
        valid_form = user_form.is_valid() #calling it here so I can access the clean data below
        valid_company = data['name']
        valid_location = data['country'] and data['state'] and data['city']

        if valid_form and valid_company and valid_location:

            location = models.Location.objects.create(country=data['country'],state=data['state'],city=data['city'])
            company = None
            try:
                company = models.Company.objects.get(name__iexact=data['name'])

            except ObjectDoesNotExist:
                company = models.Company.objects.create(name=data['name'])

            if post_id:
                model = model_dict[post_type]
                post = get_object_or_404(model, pk=post_id)
                user_form = Form(request.POST, instance=post) 
            
            post = user_form.save(commit=False)
            post.author = User.objects.get(username=request.user)
            post.location = location
            post.company = company
            post.save()
            
            redirecturl = '/gethired/post/' + post_type + '/' + str(post.pk) +'/'
            return HttpResponseRedirect(redirecturl)
        else:
            if post_type == "interview":
                user_form.fields['offer_details'].queryset = models.Offer.objects.filter(author = request.user)
            context_dict['form'] = user_form
            context_dict['post_id'] = str(post_id)
            context_dict['location_form'] = forms.LocationForm({'country':data['country'],'state':data['state'],'city':data['city']})
            context_dict['company_form'] = forms.CompanyForm({'name':data['name']})
            context_dict['post_type'] = post_type
            context_dict['companies'] = models.Company.objects.order_by('name')
            logging.debug(user_form)
            return render_to_response('gethired/newpost.html',context_dict, context)

def delete_post(request, post_type, post_id):
    if request.method == 'POST':
        Model = model_dict[post_type]
        post = get_object_or_404(Model, pk=post_id)
        post.deleted = True
        post.save()

        redirect = "/index/"
        if post_type == "interview" or post_type == "offer":
            redirect = "/gethired/"
        elif post_type == "project":
            redirect = "/marketplace/"

        return HttpResponseRedirect(redirect)

def filter_posts_gethired(request):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        data = request.GET
        
        filters = {}
        
        if 'post_type' in data:
            models_requested = data.getlist('post_type')    
        else:
            models_requested = ['interview','offer']

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
        context_dict['filters'] = get_filters_gethired()
        return render_to_response('gethired/postlist.html',context_dict,context)

def filter_posts_marketplace(request):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        data = request.GET
        
        filters = {}

        if 'location' in data and data['location'] != 'ALL':
            filters['location__state'] = data['location']

        if 'technology' in data and data['technology'] != 'ALL':
            filters['technologies__name'] = data['technology']
        all_posts = []
        all_posts.extend(models.Project.objects.filter(**filters))
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
        context_dict['filters'] = get_filters_marketplace()
        return render_to_response('marketplace/postlist.html',context_dict,context)
     
def get_company_json_list(request):
    if request.method == 'GET':
        all_posts = models.Company.objects.values_list('name', flat= True).order_by('name') 
        #convert unicode to string
        string_list = []
        for p in all_posts:
            string_list.append(p.encode('ascii','ignore'))

        return HttpResponse(simplejson.dumps(string_list),
                            content_type="application/json")

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
    
class registrationview(RegistrationView):
    form_class = forms.RegistrationFormZ

@login_required
def userprofile(request):
    context = RequestContext(request)
    context_dict = {}
    poster = models.User.objects.get(username=request.user)
    interview_posts = models.Interview.objects.filter(author=poster)
    offer_posts = models.Offer.objects.filter(author=poster)
    all_hired_posts = sorted(
                       chain(interview_posts,offer_posts),
                       key=lambda post: post.date_posted,
                       reverse = True
                      )
    all_project_posts = models.Project.objects.filter(author=poster).order_by('date_posted').reverse()
    context_dict['gethired_posts'] = all_hired_posts
    context_dict['project_posts'] = all_project_posts
    return render_to_response('portal/profile.html', context_dict, context)

def create_post_project(request):
    Form = forms.ProjectForm
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        data = request.POST
        user_form = Form(request.POST)
        location = None
        
        valid_form = user_form.is_valid() #calling it here so I can access the clean data below
        valid_location = data['country'] and data['state'] and data['city']
        valid_date = True

        if data['end_date']:
            valid_date = data['start_date'] <= data['end_date']

        if valid_form and valid_location and valid_date:
            location = models.Location.objects.create(country=data['country'],state=data['state'],city=data['city'])
            post = user_form.save(commit=False)
            m = hashlib.md5()
            m.update(post.password)
            if request.user.is_authenticated():
                post.password = request.user.username + "#*$%*$#(%$#%&(" + request.user.email
            else:
                post.password = m.hexdigest()
            if request.user.is_authenticated():
                post.author = User.objects.get(username=request.user)
            else:
                post.author = None
            post.location = location
            post.save()
            
            redirecturl = '/marketplace/post/project/' + str(post.pk) +'/'
            return HttpResponseRedirect(redirecturl)
        else:
            if not valid_date:
                errors = user_form._errors.setdefault("end_date",ErrorList())
                errors.append(u"End date cannot be before start date")
            context_dict['form'] = user_form
            context_dict['location_form'] = forms.LocationForm({'country':data['country'],'state':data['state'],'city':data['city']})
            return render_to_response('marketplace/newpost.html',context_dict, context)
    else:
        context_dict['form'] = Form()
        context_dict['location_form'] = forms.LocationForm()

        return render_to_response('marketplace/newpost.html',context_dict, context)

def edit_post_password_project(request, post_id, edit_or_delete):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'GET':
        context_dict['header'] = 'Edit '
        context_dict["post"] = post_id
        context_dict["edit_or_delete"] = edit_or_delete
        return render_to_response('marketplace/marketplace_post_password.html', context_dict, context)
    if request.method == 'POST':
        project = models.Project.objects.get(pk=post_id)
        data = request.POST
        m = hashlib.md5()
        m.update(data['password'])
        if m.hexdigest() == project.password:
            request.session['access' + post_id] = True
            return redirect('edit_post_project', post_id=post_id)
        else:
            context_dict["post"] = post_id
            context_dict["errors"] = "Wrong Password"
            return render_to_response('marketplace/marketplace_post_password.html', context_dict, context)

def delete_password_project(request,post_id):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        project = models.Project.objects.get(pk=post_id)
        data = request.POST
        m = hashlib.md5()
        m.update(data['password'])
        if m.hexdigest() == project.password:
            request.session['access' + post_id] = True
            project.deleted = True
            project.save()

            return HttpResponseRedirect("/marketplace/")
        else:
            context_dict["post"] = post_id
            context_dict["errors"] = "Wrong Password"
            return render_to_response('marketplace/marketplace_post_password.html', context_dict, context)

def edit_post_project(request, post_id):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'GET':
        project = models.Project.objects.get(pk=post_id)
        if request.user == project.author or request.session['access' + post_id] == True:
            form = forms.ProjectForm
            context_dict['form'] = form(instance=project)
            context_dict['location_form'] = forms.LocationForm(instance=project.location)
            context_dict['update'] = True
            context_dict['post_id'] = post_id
            context_dict['header'] = 'Edit '
            context_dict['post_type'] = "project"
            return render_to_response('marketplace/newpost.html', context_dict, context)
        else:
            return redirect('get_post_project', post_id=post_id)
    if request.method == 'POST':
        project = models.Project.objects.get(pk=post_id)
        if request.user == project.author or request.session['access' + post_id] == True:
            project = models.Project.objects.get(pk=post_id)
            form = forms.ProjectForm
            user_form = form(request.POST, instance=project)
            data = request.POST
            cleaned_desc = BeautifulSoup(data['description'])
            user_form.description = cleaned_desc.prettify()
            location = None

            if request.user.is_authenticated():
                user_form.password = request.user.username + "#*$%*$#(%$#%&(" + request.user.email

            valid_form = user_form.is_valid() #calling it here so I can access the clean data below
            valid_location = data['country'] and data['state'] and data['city']
            valid_date = True

            if data['end_date']:
                valid_date = data['start_date'] <= data['end_date']

            if valid_form and valid_location and valid_date:
                post = user_form.save(commit=False)
                try:
                    post.author = User.objects.get(username=request.user)
                except ObjectDoesNotExist:
                   post.author = None
                location = models.Location.objects.create(country=data['country'],state=data['state'],city=data['city'])
                post.location = location
                m = hashlib.md5()
                m.update(data['password'])
                post.password = m.hexdigest()
                post.save()
                user_form.save_m2m()
                try:
                    del request.session['access' + post_id]
                except:
                   print "session error"
                return redirect('get_post_project', post_id=post_id)
            else:
                if not valid_date:
                    errors = user_form._errors.setdefault("end_date",ErrorList())
                    errors.append(u"End date cannot be before start date")
                
                context_dict['form'] = user_form
                context_dict['post_type'] = "project"
                context_dict['update'] = True
                context_dict['post_id'] = post_id
                context_dict['header'] = 'Edit '
                context_dict['post_type'] = "project"
                context_dict['location_form'] = forms.LocationForm({'country':data['country'],'state':data['state'],'city':data['city']})
                return render_to_response('marketplace/newpost.html',context_dict, context)
    
def get_post_project(request, post_id):
    if request.method == 'GET':
        context = RequestContext(request)
        context_dict = {}
        model = model_dict["project"]
        post = get_object_or_404(model, pk=post_id)
        if post.deleted:
            raise Http404

        context_dict['post'] = post
        context_dict['related_posts'] = get_related_posts_project(post_id)

        return render_to_response('marketplace/post.html',context_dict, context)

def get_related_posts_project(post_id):
    post = models.Project.objects.get(pk=post_id)

    candidates_posts = models.Project.objects.exclude(pk=post_id, deleted=True)
    relevance = []

    for i in range(len(candidates_posts)):
        p = candidates_posts[i]
        points = 0

        if p.location == post.location: points+=1 
        t1 = set(p.technologies.all())
        t2 = set(post.technologies.all())
        intersection = t1 & t2

        points += len(intersection)

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
    
def project_send_email(request, post_id):
    proj = models.Project.objects.get(pk=post_id)
    subject = 'Re: ' + proj.title
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        data = request.POST
        from_email =  data['from_email']
        if data['from_email'].strip() == "" or data['body'].strip() == "":
            request.session['email_error'] = True
            return redirect('contact_project', post_id=post_id)
        else:
            body = 'Hello,\n \n'
            body = body + 'You have received the following response to your post from '
            body = body + from_email + ':\n' + 'Message: \n \n' + data['body'] +'\n'
            body = body +'\n This email was sent from your post at http://studentportal.cs.unc.edu/marketplace/post/project/'
            body = body + post_id + '\n \n'
            to_email = proj.email
            email = EmailMessage(subject, body, from_email, {to_email})
            email.send()
            request.session['email_error'] = False
            context_dict['success'] = True
            return HttpResponseRedirect('/marketplace/post/project/'+post_id+'/')
    else:
        context_dict['post_id'] = post_id
        context_dict['header'] = subject
        return render_to_response('marketplace/contact_project.html', context_dict, context)