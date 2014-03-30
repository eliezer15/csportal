from django.forms import ModelForm
from GetHired.models import Interview, Offer

class InterviewForm(ModelForm):
    class Meta:
        model = Interview

class OfferForm(ModelForm):
    class Meta:
        model = Offer
