'''
Created on Jul 27, 2021

@author: HP-PAVILLION
'''
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
import logging
from auth_app.rest_api.auth_api.validators import validate_register_data,\
    validate_login_data, validate_logout_data, validate_forget_password_data
from auth_app.sub_models.Users import Users
from datetime import datetime
from auth_app.rest_api.auth_api.handlers import generate_password,\
    send_password_to, generate_token
from _md5 import md5
import hashlib
from auth_app.sub_models.AuthPrivilage import AuthSerializer, AuthPrivilage


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




@api_view(['POST'])
def loginuser(request):
    try:
        print("IAM 0")
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Check whether data fields are valid
        if(validate_login_data(body)):
            # Get User data
            user_list=Users.objects.filter(UserEmail=body['email']);
            count_of_existance=user_list.count()
            print(count_of_existance)
            # If user not registered
            if(count_of_existance==0):
                return JsonResponse({'Message':"Not Registered"},status=status.HTTP_400_BAD_REQUEST)
            # User registered
            else:
                print("A")
                print(str(user_list))
                # get user object
                user=user_list.first()
                # check password
                incoming_password=hashlib.sha256(str(body['password']).encode('utf-8')).hexdigest()
                password_in_db=user.UserPassword
                # password invalid
                if(incoming_password!=password_in_db):
                    return JsonResponse({'Message':"Wrong Password"},status=status.HTTP_400_BAD_REQUEST)
                # password valid
                else:
                    print("IM D")
                    token=generate_token()
                    print("IM A")
                    tokenlist=user.Tokens
                    print(tokenlist)
                    tokenlist.append(token)
                    user.Tokens=tokenlist
                    print("IM B")
                    user.save()
                    
                    
                    auth_serializer=AuthSerializer(user.AuthAccess,many=True)
                    print(auth_serializer.data)
                    json_response={
                          "UserID":user.UserId,
                          "UserName":user.UserName,
                          "UserEmail":user.UserEmail,
                          "Gender":user.Gender,
                          "Age":user.UserAge,
                          "PostalCode":user.PostalCode,
                          "Token":token,
                          "Privilege":auth_serializer.data
                          }
                    return JsonResponse(json_response,status=status.HTTP_200_OK)
        else:
            # Invalid Fields
            return JsonResponse({'Message':"Validation Failed"},status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        # Unexpected Exception Occured
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['POST'])
def logout(request):
    try:
        print("IAM 0")
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Check whether data fields are valid
        if(validate_logout_data(body)):
            # Get User data
            user_list=Users.objects.filter(UserEmail=body['email']);
            count_of_existance=user_list.count()
            print(count_of_existance)
            # If user not registered
            if(count_of_existance==0):
                return JsonResponse({'Message':"Not Registered"},status=status.HTTP_400_BAD_REQUEST)
            # User registered
            else:
                print(str(user_list))
                # get user object and token value
                user=user_list.first()
                token=body['Token']
                print(token)
                # get token object of the value
                token_found=False
                token_obj=None
                for token_dict in user.Tokens:
                    if token_dict['value']==token:
                        token_found=True
                        token_obj=token_dict
                        break
                    
                if not(token_found):
                    return JsonResponse({'Message':"Already Logged Out"},status=status.HTTP_400_BAD_REQUEST)
                # password valid
                else:
                    user.Tokens.remove(token_obj)
                    user.save()
                    return JsonResponse({"Message": "logged out Successfully"},status=status.HTTP_200_OK)
        else:
            # Invalid Fields
            return JsonResponse({'Message':"Validation Failed"},status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        # Unexpected Exception Occured
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def forget_password(request):
    try:
        print("IAM 0")
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Check whether data fields are valid
        if(validate_forget_password_data(body)):
            # Get User data
            user_list=Users.objects.filter(UserEmail=body['email']);
            count_of_existance=user_list.count()
            print(count_of_existance)
            # If user not registered
            if(count_of_existance==0):
                return JsonResponse({'Message':"Not Registered"},status=status.HTTP_400_BAD_REQUEST)
            # User registered
            else:
                print(str(user_list))
                # get user object and token value
                user=user_list.first()
                
                password = generate_password()
                # Assign Password
                user.UserPassword=hashlib.sha256(str(password).encode('utf-8')).hexdigest()
                print("IAM 2")
                # Send Password via a mail
                send_password_to(user,password)
                # Save user to MongoDB
                user.save()
                
                return JsonResponse({"Message": "New Password Sent to Email Successfully"},status=status.HTTP_200_OK)
        else:
            # Invalid Fields
            return JsonResponse({'Message':"Validation Failed"},status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        # Unexpected Exception Occured
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


 