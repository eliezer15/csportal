'''
Created on Mar 18, 2014

@author: encarnae
A simple dict which will be useful
to define which type of post is being requested by the client '''

from GetHired import models, forms

model_dict = {
             "interview": models.Interview,
             "offer": models.Offer,
             "company": models.Company,
             "location": models.Location
}

form_dict = {
            "interview": forms.InterviewForm,
            "offer": forms.OfferForm
}

