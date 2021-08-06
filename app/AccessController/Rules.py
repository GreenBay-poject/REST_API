from functools import wraps
from django.http.response import JsonResponse
from rest_framework import status
from app.Models.Users import Users
import json
from app.AccessController.Roles import *




def role_required(allowed_roles):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            
            # Logic For All Users
            if allowed_roles==ALLOWS_ALL:
                return view_func(request, *args, **kwargs)
            
            # Logic For General And Ministry Users (Only Need Valid Token)
            if allowed_roles==ALLOWS_REGULAR_AND_MINISTRY_USERS:
                token_status=token_valid(request)
                if token_status==True:
                    return view_func(request, *args, **kwargs)
                else:
                    return JsonResponse({"Message":token_status},status=status.HTTP_400_BAD_REQUEST)
            
            # Private Function (No One Has Permission TO Access)
            else:
                return JsonResponse({"Message":"Private Function"},status=status.HTTP_400_BAD_REQUEST)
                
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
    #email registered
    user_list=Users.objects.filter(UserEmail=body['email']);
    count_of_existance=user_list.count()
    if(count_of_existance==0):
        return 'User Not Registered'
    
    # token valid
    user=user_list.first()
    token=body['Token']
    token_found=False
    for token_dict in user.Tokens:
        if token_dict['value']==token:
            token_found=True
            break
    if not(token_found):
        return 'TOKEN INVALID'
                
    # No Issued Found      
    return True