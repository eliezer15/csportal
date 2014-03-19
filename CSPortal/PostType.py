'''
Created on Mar 18, 2014

@author: encarnae
A simple enum-like list of variables with numeric values, which will be useful
to define which type of post is being requested by the client '''

from GetHired import models

INTERVIEW = 1
OFFER = 2

model_dict = {
             INTERVIEW: models.Interview,
             OFFER: models.Offer
}

    
    