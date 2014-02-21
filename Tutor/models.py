from django.db import models

class Post(models.Model):
    Title = models.CharField(max_length=128)
    Fname = models.CharField(max_length=128)
    Lname = models.CharField(max_length=128)
    Email = models.EmailField(max_length=75)
    Course = models.ForeignKey('Classes')
    Description = models.TextField()
    Compensation = models.CharField(max_length=15)
    SeekingorOffering = models.ForeignKey('SOO')
    Password = models.CharField(max_length=128)
    Added = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.Fname

class Classes(models.Model):
    ClassName = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.ClassName

class SOO(models.Model):
    Type = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.Type