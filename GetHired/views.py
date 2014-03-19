from GetHired.models import Interview, Offer
from django.template import  RequestContext
from django.shortcuts import render_to_response
from itertools import chain
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
    context_dict['posts'] = all_posts
        
    return render_to_response('portal/index.html', context_dict, context)
