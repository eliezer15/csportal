from django import forms
from django.forms.extras.widgets import SelectDateWidget
from GetHired.models import Interview, Offer, GetHiredPost, Location, Company

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        exclude = ["author"]

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ["author"]

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company

