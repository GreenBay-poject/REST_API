'''
Created on Jul 30, 2021

@author: HP-PAVILLION
'''

from functools import wraps
from django.http.response import JsonResponse
from rest_framework import status
from auth_app.access_controllers.roles import ALLOWS_ALL,\
    ALLOWS_REGULAR_AND_MINISTRY_USERS
from auth_app.sub_models.Users import Users
import json

def role_required(allowed_roles):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if allowed_roles==ALLOWS_ALL:
                return view_func(request, *args, **kwargs)
            if allowed_roles==ALLOWS_REGULAR_AND_MINISTRY_USERS:
                token_status=token_valid(request)
                if token_status==True:
                    return view_func(request, *args, **kwargs)
                else:
                    return JsonResponse({"Message":token_status},status=status.HTTP_400_BAD_REQUEST)
            
                
        return wrap
    return decorator

def token_valid(request):
    body=json.loads(request.body)
    
    #email field
    if('email' not in body.keys()):
        return 'Please Provide email Field'
    #token field
    if('Token' not in body.keys()):
        return 'Please Provide Token Field'
    #email registeed
    user_list=Users.objects.filter(UserEmail=body['email']);
    count_of_existance=user_list.count()
    if(count_of_existance==0):
        return 'User Not Registered'
    # token valid
    user=user_list.first()
    token=body['Token']
    token_found=False
    token_obj=None
    for token_dict in user.Tokens:
        if token_dict['value']==token:
            token_found=True
            token_obj=token_dict
            break
                    
    if not(token_found):
        return 'TOKEN INVALID'
                
    return True