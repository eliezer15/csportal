from django import forms
from GetHired.models import Interview, Offer, GetHiredPost, Location, Company

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city','state')

