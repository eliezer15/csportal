import os
from random import choice, randint
from models import Offer, Interview, Location, Company
from django.contrib.auth.models import User
def populate():
    companies = Company.objects.all();
    locations = Location.objects.all();
    user = User.objects.get(username='root')
    degree = ['MI','BA','BS']
    title = ['SE','WD','ST','DE','BA','CO']
    job_type = ['FT','PT','PI','CO']
    pay_type = ['YS','MS']
    salaries = [50000, 60000, 70000, 80000]
    bonus = [3000, 10000, 5000]
    offer_status = ['AC','NA','NE','WA']
	
	
    interview_process = "Submitted my resume through my school's career center. Contacted a couple weeks later to schedule a phone interview. Couldn't understand the interviewer. Was notified via email a few weeks later that I was not selected for the final round. "

    questions = '''What are your strengths?
What are your weaknesses?
Where do you see yourself in 5 years?
What is your salary expectation?'''
    
    interview_source = ['CF','AO','RE']
    interview_offer = ['RC','NR','WA']
	
    for i in range(0,20):
        add_Interview(user,
                      choice(degree),
                      choice(companies),
                      choice(locations),
                      choice(title),
                      choice(job_type),
                      interview_process,
                      questions,
                      choice(interview_source),
                      choice(interview_offer),
                      randint(1,5))


def add_Interview(user, degree, company, location, title, type, process, questions, source, status, rating):
    p = Interview.objects.create(author= user, 
								 applicant_degree = degree, 
                                 company = company,
                                 location = location,
                                 job_title = title,
                                 job_type = type,
                                 interview_process = process,
                                 questions_asked = questions,
                                 interview_source = source,
                                 offer_status = status,
                                 offer_details = None,
                                 interview_rating = rating)

'''
def add_Offer(user, degree, company, location, title, type, process, questions, source, status, rating):
    p = Offer.objects.create(author= user, 
								 applicant_degree = degree, 
                                 company = company,
                                 location = location,
                                 job_title = title,
                                 job_type = type,
                                 interview_process = process,
                                 questions_asked = questions,
                                 interview_source = source,
                                 offer_status = status,
                                 offer_details = None,
                                 interview_rating = rating)
'''

	
# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSPortal.settings")
    populate()
