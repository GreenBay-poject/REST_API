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

def validate_login_data(body):
    if('email' not in body.keys()):
        return False
    if('password' not in body.keys()):
        return False
    
    return True

def validate_logout_data(body):
    if('email' not in body.keys()):
        return False
    if('Token' not in body.keys()):
        return False
    
    return True

def validate_forget_password_data(body):
    if('email' not in body.keys()):
        return False
    
    return True

