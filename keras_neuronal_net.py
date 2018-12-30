# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:58:49 2018

The setup up of the model and the trainig and 
the saving of the results

@author: Wolfgang Kapferer
"""

from keras.layers import Dense
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.models import model_from_json
import matplotlib.pyplot as plt
import numpy as np

def run_model(preprocessed):

    model=np.float32(preprocessed)
    
    input_model=model[:,1:len(model[0])-1]
    result_model=model[:,len(model[0])-1]
    
    model = Sequential()
    
    model.add(Dense(100, use_bias=True, activation='sigmoid', input_dim=168))
    model.add(BatchNormalization(axis=-1))
    
    model.add(Dense(1, use_bias=True, activation='sigmoid'))
    
    model.compile(optimizer='SGD',
                  loss='mean_absolute_error',
                  metrics=['accuracy'])
    
    model.summary()
    
    history = model.fit(input_model, result_model, 
              validation_split=0.8,  shuffle=True, 
              epochs=3, batch_size=32)
    
    #list all preprocessed in history
    print(history.history.keys())
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    
    
    # evaluate the model
    scores = model.evaluate(input_model, result_model, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    
    # serialize model to JSON
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")
     
