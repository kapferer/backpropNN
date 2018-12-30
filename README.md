
# Example for a backpropagation Neuronal Network with Keras and TensorFlow
An example-implementation for a backpropagation Neuronal Network with Keras and TensorFlow. It reads data from an EXASOL database and stores the result in the database.

Data from https://archive.ics.uci.edu/ml/datasets/bank+marketing

## predictorMain.py
A simple python programm for a backprop Neuronal Network with
KERAS and TensorFlow

## database_import.py
Use the database EXASOL and get some data into the appropriate shape

## preprocess_database_resultset.py
precprocessing of data
data -> the input data
columnsForEncode -> which columns host categorical data for one-hot encoding
resultColumns > this data will be trained for, later on predicted, when network is used
pKcolumns -> the primary Keys for storage of the results

## keras_neuronal_net.py
The setup up of the model, trainig and 
the saving of the results

## keras_load_model_and_apply.py
loads a trained model an use it on preprocessed data

## write_into_database.py
writes data into the database

