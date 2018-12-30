# -*- coding: utf-8 -*-
"""
Created on Sun June 08 08:37:39 2018

A simple python prgramm for a backprop Neuronal Network with
KERAS and TensorFlow

@author: Wolfgang Kapferer
"""

import database_import
import preprocess_database_resultset
import keras_neuronal_net
import keras_load_model_and_apply
import write_into_database

#The data SQL                
sql = "SELECT * FROM DATEN.UCI_FESTGELD"

#Fetch the data
data = database_import.database_read(sql)

#preprocess the data for usage with neuronal network
#prepare_database_data(data, columnsForEncode [one hot],
#resultColumns [the result to train],
#pKcolumns [the primary Keys]):
preprocessed = preprocess_database_resultset.prepare_database_data(data,[2,3,4,
                                            5,7,8,9,10,11,11,13,15,16], [17], [0])

#the neuronal network training
keras_neuronal_net.run_model(preprocessed)

#load a trained network and apply it to preprocesed data
prediction=keras_load_model_and_apply.load_model_and_apply(preprocessed)

#write the prediction into the database
write_into_database.database_write(prediction)
