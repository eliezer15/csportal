import os

def populate():
    comp_class = add_class(name="Comp431")
    comp531_class = add_class(name="Comp531")
    comp550_class = add_class(name="Comp550")
    Seeking = add_type(type="Seeking")
    Offering = add_type(type="Offering")
    
    add_Post(title="My first Post!",
            fname="Danyal", 
            lname="Fiza", 
            email="dan.fiza@yahoo.com", 
            course=comp_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Seeking,
            password="test1")
    
    add_Post(title="My Second Post!",
            fname="Red", 
            lname="Deer", 
            email="dan.fiza@yahoo.com", 
            course=comp531_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test2")
    
    add_Post(title="My Third Post!",
            fname="Deer", 
            lname="Green", 
            email="Deer.Greenza@yahoo.com", 
            course=comp550_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test3")

    add_Post(title="My first Post!",
            fname="Danyal", 
            lname="Fiza", 
            email="dan.fiza@yahoo.com", 
            course=comp_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Seeking,
            password="test1")
    
    add_Post(title="My Second Post!",
            fname="Red", 
            lname="Deer", 
            email="dan.fiza@yahoo.com", 
            course=comp531_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test2")
    
    add_Post(title="My Third Post!",
            fname="Deer", 
            lname="Green", 
            email="Deer.Greenza@yahoo.com", 
            course=comp550_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test3")
    add_Post(title="My first Post!",
            fname="Danyal", 
            lname="Fiza", 
            email="dan.fiza@yahoo.com", 
            course=comp_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Seeking,
            password="test1")
    
    add_Post(title="My Second Post!",
            fname="Red", 
            lname="Deer", 
            email="dan.fiza@yahoo.com", 
            course=comp531_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test2")
    
    add_Post(title="My Third Post!",
            fname="Deer", 
            lname="Green", 
            email="Deer.Greenza@yahoo.com", 
            course=comp550_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test3")
    add_Post(title="My first Post!",
            fname="Danyal", 
            lname="Fiza", 
            email="dan.fiza@yahoo.com", 
            course=comp_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Seeking,
            password="test1")
    
    add_Post(title="My Second Post!",
            fname="Red", 
            lname="Deer", 
            email="dan.fiza@yahoo.com", 
            course=comp531_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test2")
    
    add_Post(title="My Third Post!",
            fname="Deer", 
            lname="Green", 
            email="Deer.Greenza@yahoo.com", 
            course=comp550_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test3")
    add_Post(title="My first Post!",
            fname="Danyal", 
            lname="Fiza", 
            email="dan.fiza@yahoo.com", 
            course=comp_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Seeking,
            password="test1")
    
    add_Post(title="My Second Post!",
            fname="Red", 
            lname="Deer", 
            email="dan.fiza@yahoo.com", 
            course=comp531_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test2")
    
    add_Post(title="My Third Post!",
            fname="Deer", 
            lname="Green", 
            email="Deer.Greenza@yahoo.com", 
            course=comp550_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test3")
    add_Post(title="My first Post!",
            fname="Danyal", 
            lname="Fiza", 
            email="dan.fiza@yahoo.com", 
            course=comp_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Seeking,
            password="test1")
    
    add_Post(title="My Second Post!",
            fname="Red", 
            lname="Deer", 
            email="dan.fiza@yahoo.com", 
            course=comp531_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test2")
    
    add_Post(title="My Third Post!",
            fname="Deer", 
            lname="Green", 
            email="Deer.Greenza@yahoo.com", 
            course=comp550_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test3")
    add_Post(title="My first Post!",
            fname="Danyal", 
            lname="Fiza", 
            email="dan.fiza@yahoo.com", 
            course=comp_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Seeking,
            password="test1")
    
    add_Post(title="My Second Post!",
            fname="Red", 
            lname="Deer", 
            email="dan.fiza@yahoo.com", 
            course=comp531_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test2")
    
    add_Post(title="My Third Post!",
            fname="Deer", 
            lname="Green", 
            email="Deer.Greenza@yahoo.com", 
            course=comp550_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test3")
    add_Post(title="My first Post!",
            fname="Danyal", 
            lname="Fiza", 
            email="dan.fiza@yahoo.com", 
            course=comp_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Seeking,
            password="test1")
    
    add_Post(title="My Second Post!",
            fname="Red", 
            lname="Deer", 
            email="dan.fiza@yahoo.com", 
            course=comp531_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test2")
    
    add_Post(title="My Third Post!",
            fname="Deer", 
            lname="Green", 
            email="Deer.Greenza@yahoo.com", 
            course=comp550_class,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac sapien dictum, interdum ante vitae, fringilla lacus. Proin ultrices interdum ipsum non vestibulum. Maecenas nisl nisi, vestibulum a porta non, lobortis hendrerit tellus. Sed quis quam neque. Cras commodo condimentum justo vitae varius. Donec varius lobortis lorem non tristique. Quisque congue ligula nec nulla tincidunt aliquam. Proin accumsan dolor turpis, nec porttitor quam fermentum et. Nam dictum vulputate ipsum ut lobortis. Proin est purus, vulputate sit amet libero eu, euismod ultricies tortor. ",
            compensation="free",
            seekingoroffering = Offering,
            password="test3")

    # Print out what we have added to the user.
    for c in Classes.objects.all():
        print format(str(c))
    for p in Post.objects.all():
        print format(str(p))
        
def add_Post(title, fname, lname, email, course, description, compensation, seekingoroffering, password):
    p = Post.objects.create(Title= title, Fname = fname, Lname = lname, Email = email, 
                                    Course = course, Description = description, Compensation = compensation,
                                    SeekingorOffering = seekingoroffering, Password=password)
    return p

def add_class(name):
    c = Classes.objects.get_or_create(ClassName=name)[0]
    return c

def add_type(type):
    t = SOO.objects.get_or_create(Type=type)[0]
    return t
# Start execution here!
if __name__ == '__main__':
    print "Starting tutors population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSWebPortalMock.settings")
    from Tutor.models import Post, Classes, SOO
    populate()