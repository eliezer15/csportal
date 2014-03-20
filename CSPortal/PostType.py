'''
Created on Mar 18, 2014

@author: encarnae
A simple dict which will be useful
to define which type of post is being requested by the client '''

from GetHired import models

model_dict = {
             "Interview": models.Interview,
             "Offer": models.Offer
}

    
    
