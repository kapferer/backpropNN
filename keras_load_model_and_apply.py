# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:38:34 2018

load a trained model an use it on preprocessed data

@author: Wolfgang Kapferer
"""
from keras.models import model_from_json
import numpy as np

def load_model_and_apply(preprocessed):

    resultForDatabase=[]
    
    model=np.float32(preprocessed)
    
    input_model=model[:,1:len(model[0])-1]
    
    pk = model[:,0]
    resultForDatabase.append(pk)
    
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
     
    prediction = loaded_model.predict(input_model)
    resultForDatabase.append(prediction)
    
    return resultForDatabase
