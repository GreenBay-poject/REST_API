'''
Created on Jul 27, 2021

@author: HP-PAVILLION
'''
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
import logging
from auth_app.rest_api.auth_api.validators import validate_register_data
from auth_app.sub_models.Users import Users
from datetime import datetime
from auth_app.rest_api.auth_api.handlers import generate_password,\
    send_password_to
from _md5 import md5
import hashlib


@api_view(['POST'])
def registeruser(request):
    try:
        print("IAM 0")
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Check whether data fields are valid
        if(validate_register_data(body)):
            # Check whether user registered before
            count_of_existance=Users.objects.filter(UserEmail=body['email']).count()
            print(count_of_existance)
            # If user already registred
            if(count_of_existance>0):
                return JsonResponse({'Message':"Already Registered"},status=status.HTTP_400_BAD_REQUEST)
            # User not registered before
            else:
                # Create user object
                user=Users()
                user.UserName=body['name'] 
                user.UserEmail=body['email'] 
                user.UserAge=body['age'] 
                user.Gender=body['gender'] 
                user.PostalCode=body['postalcode']
                user.DateRegistered=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                user.QuestionList=[]
                user.Notes=[]
                user.Tokens=[]
                user.AuthAccess=[]
                # Generate Password 
                password = generate_password()
                # Assign Password
                user.UserPassword=hashlib.sha256(str(password).encode('utf-8')).hexdigest()
                print("IAM 2")
                # Send Password via a mail
                send_password_to(user,password)
                # Save user to MongoDB
                user.save()
                print("IAM 3")
                # Registered Success !
                return JsonResponse({'content':str(request.body)},status=status.HTTP_200_OK)
        else:
            # Invalid Fields
            return JsonResponse({'Message':"Validation Failed"},status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        # Unexpected Exception Occured
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        