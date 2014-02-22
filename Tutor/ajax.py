from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from Tutor.models import Post
from Tutor.forms import PostForm
from django.template.loader import render_to_string
from dajaxice.utils import deserialize_form
from dajax.core import Dajax

#This method handles the get requests from each link
#in the posting list, jquery is used to grab the primary key of the
#post which is embedded in the link and used to get the object which is then placed in
#the context dictionary, and sent to the post.html file to be injected and rendered into
#a string which is then passed through ajax to the callback function in the tutor-ajax file
#and is inserted into the #contentDiv on the index page through javascript

@dajaxice_register(method='GET', name='post.get')
def post(request, p_id):
    context_dict = {}
    if request.method == 'GET':
        if p_id:
            post = Post.objects.filter(id=p_id)
            context_dict['post'] = post
            render = render_to_string('tutor/post.html', context_dict)
    return simplejson.dumps({'post': render})

#This method handles the ajax get request issued by clicking the Add Post button
#on the homepage. It will simply get a PostForm model from the form.py file and send 
#that object to the newpost.html file to be injected and rendered to a string which is then
#sent as a json object to javascript to be inserted into the #contentDiv

@dajaxice_register(method='GET', name='new_post.get')
def new_post(request):
    if request.method == 'GET':
        form = PostForm()
        render = render_to_string('tutor/newpost.html', {'form': form})
        return simplejson.dumps({'form': render})

#This method handles the ajax post request which validates the new post form injected by the previous
#method. This will convert the form into a python model, check if it is valid. If it is valid it will save
#the form into a Post model and reload the index page. If not valid, the form model will be sent to the newpost.html
#file to be injected and proper error messages will be added and sent back to the user, this time using dajax instead of sending 
#a json file. Once the user sees errors, they can correct and submit agian to be validated by this method again.

@dajaxice_register
def val_post(request, form):
    dajax = Dajax()
    form = PostForm(deserialize_form(form))

    if form.is_valid():
        form.save()
        dajax.alert("You have posted!")
        dajax.redirect('', delay=20)
    else:
        render = render_to_string('tutor/newpost.html', {'form': form})
        dajax.clear('#contentDiv', 'innerHTML')
        dajax.append('#contentDiv', 'innerHTML', render)
        dajax.script('styleInputs();')
    return dajax.json()

#This method handles the request to edit a post, this method is called when the user clicks the edit button in a post
#Javascript will grab the id from the post and have it sent to this method to inject the id into the pass.html template 
#into a hidden div and send the password request template over to the users contextDiv which is again injected through json and jquery

@dajaxice_register(method='GET', name='edit_post_pass.get')
def edit_post_pass(request, p_id):
    if request.method == 'GET':
        context_dict = {}
        context_dict['post'] = p_id
        render = render_to_string('tutor/pass.html', context_dict);
        return simplejson.dumps({'pass': render})

#This method will handle checking if the password is correct to the post that is being requested to edit
#if valid the method will get the object requesting to be edited, place it into the postform model to have the values
#be placed into the place holders and then rendered to a string and sent over through json where jquery will inject the string 
#into the contentDiv. If the pass is not valid, the user will simply be given an error message

@dajaxice_register(method='POST', name='check_pass.post')    
def check_pass(request, p_id, passw):
    if request.method == 'POST':
        if p_id:
            posts = Post.objects.filter(id=p_id)
            for post in posts:
                if passw == post.Password:
                    form = PostForm(instance=post)
                    render = render_to_string('tutor/newpost.html', {'form': form,'update': "True",'id': p_id})
                    return simplejson.dumps({'form': render})
                else: 
                    return simplejson.dumps({'Error': "Password is incorrect."});
                
#This method will be used once the user preses the update post button, which is after they have succesfully logged in
#to edit their post. This will check if the form is valid, if it is, the post will be updated and the confirmation message
#will be sent through json where the callback function in tutor-ajax will handle redirecting and refreshing of the page. If the post
#is not valid the postform will again be sent to newpost to be injected and proper errors be handled and be rendered to a string
#which will be sent through json and injected by the callback function

@dajaxice_register(method='POST', name='update_post.post')
def update_post(request, form, p_id):
    
    print p_id
    posts = Post.objects.filter(id=p_id)
    for post in posts:
        form = PostForm(deserialize_form(form), instance=post)
        if form.is_valid():
            form.save()
            return simplejson.dumps({'posted': True})
        else:
            render = render_to_string('tutor/newpost.html', {'form': form, 'update': "True",'id': p_id})
            return simplejson.dumps({'form': render})

#This function handles the delete post request from the delete_post called from the java script file
#We will pass in the p_id and passw arguments sent over, grab the appropriate post from its id and check
#the password. If the password is correct, we will delete the field and send over a json object with the
#delete field. Else if it is incorrect we will send of a json object with the password error.

@dajaxice_register(method='POST', name='delete_post.post')
def delete_post(request, p_id, passw):
    if request.method == 'POST':
        if p_id:
            posts = Post.objects.filter(id=p_id)
            for post in posts:
                if passw == post.Password:
                    post.delete()
                    return simplejson.dumps({'deleted': True})
                else: 
                    return simplejson.dumps({'error': "Password is incorrect."});