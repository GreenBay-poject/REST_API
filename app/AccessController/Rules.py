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
            # Logic For General And Ministry Users (Only Need Valid Token)
            if allowed_roles==ALLOWS_MINISTRY_USERS_ONLY:
                token_status=authorized_token_valid(request)
                if token_status==True:
                    return view_func(request, *args, **kwargs)
                else:
                    return JsonResponse({"Message":token_status},status=status.HTTP_400_BAD_REQUEST)
            if allowed_roles==ALLOWS_GENERAL_USERS_ONLY:
                token_status=general_token_valid(request)
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
    token=request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    
    print("0"+token)
    #email field
    if('email' not in body.keys()):
        return 'Please Provide email Field'
    #token field
    if(token==""):
        return 'Please Provide Token Field'
    #email registered
    user_list=Users.objects.filter(UserEmail=body['email']);
    count_of_existance=user_list.count()
    if(count_of_existance==0):
        return 'User Not Registered'
    
    # token valid
    user=user_list.first()
    token_found=False
    for token_dict in user.Tokens:
        if token_dict['value']==token:
            token_found=True
            break
    if not(token_found):
        return 'TOKEN INVALID'
                
    # No Issued Found      
    return True


def authorized_token_valid(request):
    body=json.loads(request.body)
    token=request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    print("1"+token)
    #email field
    if('email' not in body.keys()):
        return 'Please Provide email Field'
    #token field
    if(token==""):
        return 'Please Provide Token Field'
    #email registered
    user_list=Users.objects.filter(UserEmail=body['email']);
    count_of_existance=user_list.count()
    if(count_of_existance==0):
        return 'User Not Registered'
    
    # token valid
    user=user_list.first()
    token_found=False
    for token_dict in user.Tokens:
        if token_dict['value']==token:
            token_found=True
            break
    if not(token_found):
        return 'TOKEN INVALID'
           
    if not user.get_is_auhtorized():
        return 'Sorry No Access, authorized users only'
    # No Issued Found      
    return True

def general_token_valid(request):
    body=json.loads(request.body)
    token=request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    print("2"+token)
    #email field
    if('email' not in body.keys()):
        return 'Please Provide email Field'
    #token field
    if(token==""):
        return 'Please Provide Token Field'
    #email registered
    user_list=Users.objects.filter(UserEmail=body['email']);
    count_of_existance=user_list.count()
    if(count_of_existance==0):
        return 'User Not Registered'
    
    # token valid
    user=user_list.first()
    token_found=False
    for token_dict in user.Tokens:
        if token_dict['value']==token:
            token_found=True
            break
    if not(token_found):
        return 'TOKEN INVALID'
           
    if user.get_is_auhtorized():
        return 'Sorry No Access, General users only'
    # No Issued Found      
    return True