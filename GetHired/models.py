'''
Created on Mar 18, 2014

@author: encarnae
'''
from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
#Post is an abstract class that serves as a superclass
class Post(models.Model):
    #related_name is required for all abstract classes with ForeignKey fields. See Django docs for more info
    author = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_user")
    url_slug = models.CharField(max_length=200, editable=False)
    post_type = models.CharField(max_length=20,editable=False)
    date_posted = models.DateField(auto_now_add=True) #automatically set upon object creation
    preview = models.CharField(max_length=100, null=True, blank= True,editable=False)
    def __unicode__(self):
        return self.url

    def save(self, **kwargs):
        super(Post, self).save()
        self.post_type = self.__class__.__name__
        self.url_slug = 'post/%s/%i/' % (self.post_type, self.id)
        super(Post, self).save()

    class Meta:
        abstract = True

class Company(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="companies"

class Location(models.Model):
    city = models.CharField(max_length=30)
    state = USStateField()
    country = models.CharField(max_length=30, default="United States")

    def __unicode__(self):
        return "%s, %s, %s"%(self.city, self.state, self.country)

class GetHiredPost(Post):
    degree_choices = (
            ('MI','Minor'),
            ('BA', 'B.A'),
            ('BS', 'B.S'),
            ('MA', 'M.A'),
            ('MS', 'M.S'),
            ('MB', 'MBA'),
            ('PD', 'Ph.D'),
            ('PR', 'Professional Degree'),
            ('OT','Other'),
                      )
    applicant_degree = models.CharField(max_length=2,
                                        choices=degree_choices,
                                        default='BS')
    company = models.ForeignKey(Company, related_name = "%(app_label)s_%(class)s_location")
    location = models.ForeignKey(Location, related_name="%(app_label)s_%(class)s_location")
    
    title_choices = (
        ('SE', 'Software Engineer/Developer/Programmer'),
        ('WD', 'Web Developer'),
        ('ST', 'Software Engineer in Test'),
        ('DE', 'DevOps Engineer'),
        ('BA', 'Business Analyst/Programmer Analyst'),
        ('CO', 'Consultant'),
        ('DB', 'Database Administrator'),
        ('HD', 'Help Desk Technician'),
        ('NT', 'Network Architect/Engineer'),
        ('NA', 'Network Administrator'),
        ('PM', 'Product Manager')
    )

    job_title = models.CharField(max_length=2,
                                 choices=title_choices,
                                 default='SE')

    type_choices = (
            ('FT','Full Time'),
            ('PT','Part Time'),
            ('PI','Paid Internship'),
            ('UI','Unpaid Internship'),
            ('CO','Co-op'),
            ('VW','Volunteer Work'),
            ('CC','Course Credit'),
            ('CW','Contract Work'),
            ('OT','Other'),
            )
    job_type = models.CharField(max_length=2,
                                choices=type_choices,
                                default='FT')
    
    def __unicode__(self):
        return "%s, %s, %s"%(self.author, self.company, self.location)
    
    class Meta:
        abstract = True

class Offer(GetHiredPost):
    pay_choices = (
            ('YS','Yearly Salary'),
            ('MS','Monthly Salary'),
            ('WS','Weekly Salary'),
            ('HS','Hourly Salary'),
            ('TS', 'Total Salary'),
            ('OT','Other'),
            )
    pay_type = models.CharField(max_length=2,
                                choices=pay_choices,
                                default='YS')
    salary = models.DecimalField(decimal_places=2, max_digits=8)
    signing_bonus = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    relocation_bonus = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)

    offer_choices = (
            ('AC','Accepted'),
            ('NA','Not Accepted'),
            ('NE','Negotiating'),
            ('WA','Waiting'),
            ('OT','Other'),
            )
    offer_status = models.CharField(max_length=2,
                                    choices=offer_choices,
                                    default='WA')
    other_details = models.TextField(blank=True, null=True)
    def save(self):
        self.preview = self.interview_process[:50] + '...' #sliced to 50 chars        
        super(Offer, self).save()
class Interview(GetHiredPost):
    interview_process = models.TextField()
    questions_asked = models.TextField()

    source_choices = (
            ('CF','Career Fair'),
            ('AO','Applied Online'),
            ('EF','Employee Referral'),
            ('PI','Previous Internship'),
            ('RE','Recruiting Event'),
            ('OT','Other'),
            )
    interview_source = models.CharField(max_length=2,
                                    choices=source_choices,
                                    default='WA')

    offer_choices = (
            ('RC','Received'),
            ('NR','Not Received'),
            ('WA','Waiting for Offer'),
            )
    offer_status = models.CharField(max_length=2,
                                    choices=offer_choices,
                                    default='WA')
    offer_details = models.OneToOneField(Offer, null=True, blank=True)
    interview_rating = models.IntegerField()
    
    def save(self, **kwargs):
        self.preview = self.interview_process[:100] + '...' #sliced to 50 chars        
        super(Interview, self).save()


