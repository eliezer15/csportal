import os
from random import choice, randint
from models import Technology, Project, Location
from django.contrib.auth.models import User
from datetime import datetime
def populate():

    #technologies and locations
    Technology.objects.create(name='Java')
    Technology.objects.create(name='C++')
    Technology.objects.create(name='DirectX')
    Technology.objects.create(name='JavaScript')
    Technology.objects.create(name='Python')
    Technology.objects.create(name='Android')
    Technology.objects.create(name='IOS')

    Location.objects.create(city='Denver',state='CO')
    Location.objects.create(city='Madison',state='WI')
    Location.objects.create(city='Baltimore',state='MD')
    Location.objects.create(city='San Jose',state='CA')
    Location.objects.create(city='New York',state='NY')
    Location.objects.create(city='Boston',state='MA')
    Location.objects.create(city='Raleigh',state='NC')
    Location.objects.create(city='San Francisco',state='CA')

    technologies = Technology.objects.all()
    locations = Location.objects.all()
    user = User.objects.get(username='root')
    
    emails = ['encarnae@cs.unc.edu','foo@bar.com', 'leroy@jenkins.org']
    names = ['Eliezer Encarnacion', 'Danyal Fiza', 'Sasha Karpinski', 'Andrew Park']
    titles = ['New UNC Mobile app', 'Let\'s build a robot!', 'Anyone wanna learn IOS?', 'Need help building a personal site']
    description = '''This is a project that could extremely benefitial
                      for your future employability. If you can learn to 
                      do the stuff we will be doing here, you will acquire a 
                      very useful set of skills that will help you get a job
                      once you graduate.'''

    #PROJECTS
    start_date = datetime.now()

    for i in range(0,20):
        add_Project(user,
                  choice(names),
                  choice(emails),
                  choice(titles),
                  description,
                  start_date,
                  choice(locations),
                  technologies)


def add_Project(user, client, email, title, description, start_date, location, technologies):
    p = Project.objects.create(author= user,
                                client = client,
                                email = email,
                                title = title,
                                description = description,
                                start_date = start_date,
                                location = location, password="123")
    p.technologies.add(choice(technologies))
    p.technologies.add(choice(technologies))

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSPortal.settings")
    populate()  
