'''
Created on Jul 27, 2021

@author: HP-PAVILLION
'''
import email
def validate_register_data(body):
    if('name' not in body.keys()):
        return False
    if('email' not in body.keys()):
        return False
    if('age' not in body.keys()):
        return False
    if('gender' not in body.keys()):
        return False
    if('postalcode' not in body.keys()):
        return False
    
    return True