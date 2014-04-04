from django.forms import ModelForm, Form
from GetHired.models import Interview, Offer, GetHiredPost, Location, Company

class InterviewForm(ModelForm):
    class Meta:
        model = Interview

class OfferForm(ModelForm):
    class Meta:
        model = Offer

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ('city','state')

