from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
from app.Models.Users import Users
from datetime import datetime
import hashlib
from django.views.decorators.csrf import csrf_exempt
from app.Validator.Validator import require_validation
from app.Validator.RequiredFields import CHANGE_PASSWORD, REGISTER_FIELDS, LOGIN_FIELDS,\
    LOGOUT_FIELDS, FORGET_PASSWORD_FIELDS, REGISTER_AUTH_FIELDS, GET_USER_FIELDS
from app.AccessController.Rules import role_required
from app.AccessController.Roles import ALLOWS_ALL,\
    ALLOWS_REGULAR_AND_MINISTRY_USERS
from app.Helpers.Auth_Helper import generate_password, send_password_to,\
    generate_token
from app.Models.GeneralPrivilage import GeneralPrivilage
from back_end_rest_api.settings import SECRET_CODE
from app.Models.AuthPrivilage import AuthPrivilage
from app.Models.Ministry import Ministry

@csrf_exempt
@api_view(['POST'])
@require_validation(REGISTER_FIELDS)
@role_required(ALLOWS_ALL)
def registeruser(request):
    try:
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        count_of_existance=Users.objects.filter(UserEmail=body['email']).count()
        print(count_of_existance)
        # If user already registred
        if(count_of_existance>0):
            return JsonResponse({'Message':"Already Registered"},status=status.HTTP_400_BAD_REQUEST)
        # User not registered before
        else:
            # Create user object
            user=Users()
            user.set_user_name(body['name']) 
            user.set_user_email(body['email']) 
            user.set_user_age(body['age'])
            user.set_gender(body['gender'])
            user.set_postal_code(body['postalcode'])
            user.set_date_registered(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            user.set_address(body['address'])
            user.set_notes([])
            user.set_tokens([])
            # Generate Password 
            password = generate_password()
            print(password)
            # Assign Password
            user.UserPassword=hashlib.sha256(str(password).encode('utf-8')).hexdigest()
            print("IAM 2")
            
            # Create General Privilege Object,Save,GetID
            general_privilege=GeneralPrivilage()
            general_privilege.set_question_list([])
            general_privilege.save()
            # Set Object ID to User
            user.set_is_auhtorized(False)
            user.set_privilage(general_privilege.pk)
            # Send Password via a mail
            # send_password_to(user,password)
            # Save user to MongoDB
            user.save()
            print("IAM 3")
            # Registered Success !
            return JsonResponse({'content':"Successfully Registered"},status=status.HTTP_200_OK)
 
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@csrf_exempt
@api_view(['POST'])
@require_validation(LOGIN_FIELDS)
@role_required(ALLOWS_ALL)
def loginuser(request):
    try:
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Get User data
        user_list=Users.objects.filter(UserEmail=body['email']);
        count_of_existance=user_list.count()
        #print(count_of_existance)
        # Specific user object
        user=None
        # If user not registered
        if(count_of_existance==0):
            return JsonResponse({'Message':"Not Registered"},status=status.HTTP_400_BAD_REQUEST)
        # User registered
        else:
            #print("A")
            #print(str(user_list))
            # get user object
            user=user_list.first()
            # check password
            incoming_password=hashlib.sha256(str(body['password']).encode('utf-8')).hexdigest()
            password_in_db=user.get_user_password()
            # password invalid
            if(incoming_password!=password_in_db):
                return JsonResponse({'Message':"Wrong Password"},status=status.HTTP_400_BAD_REQUEST)
            # password valid
            else:
                #print("IM D")
                token=generate_token()
                #print("IM A")
                tokenlist=user.get_tokens()
                #print(tokenlist)
                tokenlist.append(token)
                user.set_tokens(tokenlist)
                #print("IM B")
                user.save()
                     
            
                return JsonResponse({"UserEmail":user.get_user_email(),"IsAuthorized":user.get_is_auhtorized(),"Token":token},status=status.HTTP_200_OK)
          
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 
 
 
 
@csrf_exempt
@api_view(['POST'])
@require_validation(LOGOUT_FIELDS)
@role_required(ALLOWS_REGULAR_AND_MINISTRY_USERS)
def logout(request):
    try:
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Get User data
        user_list=Users.objects.filter(UserEmail=body['email']);
        
        print(str(user_list))
        # get user object and token value
        user=user_list.first()
        token=request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        print(token)
        # get token object of the value
        token_found=False
        token_obj=None
        for token_dict in user.get_tokens():
            if token_dict['value']==token:
                token_found=True
                token_obj=token_dict
                break
             
        if not(token_found):
            return JsonResponse({'Message':"Already Logged Out"},status=status.HTTP_400_BAD_REQUEST)
        # password valid
        else:
            user.get_tokens().remove(token_obj)
            user.save()
            return JsonResponse({"Message": "logged out Successfully"},status=status.HTTP_200_OK)
        
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 


@csrf_exempt
@api_view(['POST'])
@require_validation(GET_USER_FIELDS)
@role_required(ALLOWS_REGULAR_AND_MINISTRY_USERS)
def get_user_details(request):
    try:
        print("OKOK")
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        print(body)
        # Get User data
        user_list=Users.objects.filter(UserEmail=body['email']);
        
        print(str(user_list))
        # get user object and token value
        user=user_list.first()
        #create response
        response={"username":user.get_user_name(),
                  "useremail":user.get_user_email(),
                  "age":user.get_user_age(),
                  "gender":user.get_gender(),
                  "address":user.get_address(),
                  "postalcode":user.get_postal_code(),
                  "registered_date":user.get_date_registered(),
                  "notes":user.get_notes(),
                  "isAuthorized":user.get_is_auhtorized(),
                  }
                
        
        
        return JsonResponse({"UserDetails": response},status=status.HTTP_200_OK)
        
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 
@csrf_exempt
@api_view(['POST'])
@require_validation(FORGET_PASSWORD_FIELDS)
@role_required(ALLOWS_ALL)
def forget_password(request):
    try:
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Get User data
        user_list=Users.objects.filter(UserEmail=body['email']);
        count_of_existance=user_list.count()
        # If user not registered
        if(count_of_existance==0):
            return JsonResponse({'Message':"Not Registered"},status=status.HTTP_400_BAD_REQUEST)
        # User registered
        else:
            print(str(user_list))
            # get user object and token value
            user=user_list.first()
            # Generate New Password
            password = generate_password()
            # Assign Password
            user.set_user_password(hashlib.sha256(str(password).encode('utf-8')).hexdigest())
            # Send Password via a mail
            send_password_to(user,password)
            # Save user to MongoDB
            user.save()
             
            return JsonResponse({"Message": "New Password Sent to Email Successfully"},status=status.HTTP_200_OK)
        
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
    
    
    
    
    
    
    
    
    
    
@csrf_exempt
@api_view(['POST'])
@require_validation(REGISTER_AUTH_FIELDS)
@role_required(ALLOWS_ALL)
def register_auth_user(request):
    try:
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        
        # Check Secret Code
        if body['secret_code']!=SECRET_CODE:
            return JsonResponse({'Message':"Secret Code Invalid"},status=status.HTTP_400_BAD_REQUEST)
        
        
        
        count_of_existance=Users.objects.filter(UserEmail=body['email']).count()
        print(count_of_existance)
        # If user already registred
        if(count_of_existance>0):
            return JsonResponse({'Message':"Already Registered"},status=status.HTTP_400_BAD_REQUEST)
        # User not registered before
        else:
            # Create user object
            user=Users()
            user.set_user_name(body['name']) 
            user.set_user_email(body['email']) 
            user.set_user_age(body['age'])
            user.set_gender(body['gender'])
            user.set_postal_code(body['postalcode'])
            user.set_date_registered(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            user.set_address(body['address'])
            user.set_notes([])
            user.set_tokens([])
            # Generate Password 
            password = generate_password()
            # Assign Password
            user.UserPassword=hashlib.sha256(str(password).encode('utf-8')).hexdigest()
            print("IAM 2")
            # Send Password via a mail
            
            # Create General Privilege Object,Save,GetID
            ministry_list=Ministry.objects.filter(ministry_name=body['ministry_name'])
            ministry_ref=-1
            if ministry_list.count()<1:
                ministry=Ministry()
                ministry.set_ministry_name(body['ministry_name'])
                ministry.save()
                ministry_ref=ministry.pk
            else:
                ministry_ref=ministry_list.first().pk
                
            
            auth_privilege=AuthPrivilage()
            auth_privilege.set_feed_posts([])
            auth_privilege.set_position(body['position'])
            auth_privilege.set_ministry_refrence(ministry_ref)
            auth_privilege.save()
            # Set Object ID to User
            user.set_is_auhtorized(True)
            user.set_privilage(auth_privilege.pk)
            # Save user to MongoDB
            send_password_to(user,password)
            user.save()
            print("IAM 3")
            # Registered Success !
            return JsonResponse({'content':"Successfully Registered"},status=status.HTTP_200_OK)
 
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
@require_validation(CHANGE_PASSWORD)
@role_required(ALLOWS_REGULAR_AND_MINISTRY_USERS)
def change_password(request):
    try:
        #Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Get User data
        user_list=Users.objects.filter(UserEmail=body['email']);
        count_of_existance=user_list.count()
        #print(count_of_existance)
        # Specific user object
        user=None
        # If user not registered
        if(count_of_existance==0):
            return JsonResponse({'Message':"Not Registered"},status=status.HTTP_400_BAD_REQUEST)
        else:
            print(str(user_list))
            # get user object and token value
            user=user_list.first()
            # Generate New Password
            password = body['new_password']
            # Assign Password
            user.set_user_password(hashlib.sha256(str(password).encode('utf-8')).hexdigest())
            # Send Password via a mail
            #send_password_to(user)
            # Save user to MongoDB
            user.save()
             
            return JsonResponse({"Message": "New Password Set Successfully"},status=status.HTTP_200_OK)
          
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
