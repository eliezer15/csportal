from django.forms import ModelForm, Form
from GetHired.models import Interview, Offer, GetHiredPost

class InterviewForm(ModelForm):
    class Meta:
        model = Interview

class OfferForm(ModelForm):
    class Meta:
        model = Offer

class FilterGetHiredForm(ModelForm):
    class Meta:
        model = GetHiredPost
