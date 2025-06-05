''' task_00_basic_serialization.py
This module demonstrates basic serialization and deserialization using the pickle module.
'''
import pickle   
def serialize_data(data, filename):
    ''' Serialize data to a file using pickle '''
    with open(filename, 'wb') as file:
        pickle.dump(data, file) 

def deserialize_data(filename):
    ''' Deserialize data from a file using pickle '''
    with open(filename, 'rb') as file:
        return pickle.load(file)
