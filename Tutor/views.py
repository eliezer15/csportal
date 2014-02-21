from Tutor.models import Post
from django.template import RequestContext
from django.shortcuts import render_to_response

#index view

def index(request):
    context = RequestContext(request)
    context_dict ={}
    try:
        posts = Post.objects.all().order_by('-Added') #Sorts the posts by date added
        
        #The following loop, we add taglines and also the approriate SOO tag
        for post in posts:
            a = post.Description
            b = a[0:90]
            post.Tagline = b + "..."
            a = post.SeekingorOffering
            post.SOOTag = a.Type.upper()    

        context_dict['posts'] = posts
    except Post.DoesNotExist:
        pass
    
    return render_to_response('tutor/index.html', context_dict, context);