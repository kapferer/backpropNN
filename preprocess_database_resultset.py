# -*- coding: utf-8 -*-
"""
Created on Sun May 13 08:52:42 2018

precprocessing of data

data -> the input data
columnsForEncode -> which columns host categorical data for one-hot encoding
resultColumns > this data will be trained for, later on predicted, when network is used
pKcolumns -> the primary Keys for storage of the results

@author: Wolfgang Kapferer
"""
import pandas as pd
import numpy
from sklearn.preprocessing import LabelEncoder


def prepare_database_data(data, columnsForEncode, resultColumns, pKcolumns):
    
    s_result=[]
    
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
          if (str(data[i][j]).replace('\'','').lstrip("-").isdigit()) == True:
              data[i][j]=float(str(data[i][j]).replace('\'',''))
    
    for i in range(0,len(data)):
        
        if (i in pKcolumns):
            s_result.append(data[i])           
        elif (i in columnsForEncode):
            s = pd.get_dummies(list(data[i]))
            for j in range(0,len(s.columns)):
                column=s.iloc[:,j]
                s_result.append(list(column))
        
        elif (i in resultColumns):
            s_result.append(LabelEncoder().fit_transform(data[i]))
                
        else:
            norm = []
            mean=numpy.mean(data[i])
            std=numpy.std(data[i])
            for k in range(0,len(data[i])):
                norm.append((data[i][k]-mean)/std)
            s_result.append(norm)
            
    return  list(map(list, zip(*s_result)))
	
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 08:52:42 2018

precprocessing of data

data -> the input data
columnsForEncode -> which columns host categorical data for one-hot encoding
resultColumns > this data will be trained for, later on predicted, when network is used
pKcolumns -> the primary Keys for storage of the results

@author: Wolfgang Kapferer
"""
import pandas as pd
import numpy
from sklearn.preprocessing import LabelEncoder


def prepare_database_data(data, columnsForEncode, resultColumns, pKcolumns):
    
    s_result=[]
    
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
          if (str(data[i][j]).replace('\'','').lstrip("-").isdigit()) == True:
              data[i][j]=float(str(data[i][j]).replace('\'',''))
    
    for i in range(0,len(data)):
        
        if (i in pKcolumns):
            s_result.append(data[i])           
        elif (i in columnsForEncode):
            s = pd.get_dummies(list(data[i]))
            for j in range(0,len(s.columns)):
                column=s.iloc[:,j]
                s_result.append(list(column))
        
        elif (i in resultColumns):
            s_result.append(LabelEncoder().fit_transform(data[i]))
                
        else:
            norm = []
            mean=numpy.mean(data[i])
            std=numpy.std(data[i])
            for k in range(0,len(data[i])):
                norm.append((data[i][k]-mean)/std)
            s_result.append(norm)
            
    return  list(map(list, zip(*s_result)))	