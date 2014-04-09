'''
Created on Mar 18, 2014

@author: encarnae
A simple dict which will be useful
to define which type of post is being requested by the client '''

from GetHired import models, forms

model_dict = {
             "Interview": models.Interview,
             "Offer": models.Offer,
             "Company": models.Company,
             "Location": models.Location
}

form_dict = {
            "Interview": forms.InterviewForm,
            "Offer": forms.OfferForm
}

