from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
from app.Models.Users import Users
from datetime import datetime
import hashlib
from django.views.decorators.csrf import csrf_exempt
from app.Validator.Validator import require_validation
from app.Validator.RequiredFields import REGISTER_FIELDS, LOGIN_FIELDS,\
    LOGOUT_FIELDS, FORGET_PASSWORD_FIELDS
from app.AccessController.Rules import role_required
from app.AccessController.Roles import ALLOWS_ALL,\
    ALLOWS_REGULAR_AND_MINISTRY_USERS
from app.Helpers.Auth_Helper import generate_password, send_password_to,\
    generate_token
from app.Models.GeneralPrivilage import GeneralPrivilage

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
            # Assign Password
            user.UserPassword=hashlib.sha256(str(password).encode('utf-8')).hexdigest()
            print("IAM 2")
            # Send Password via a mail
            send_password_to(user,password)
            # Create General Privilege Object,Save,GetID
            general_privilege=GeneralPrivilage()
            general_privilege.set_question_list([])
            general_privilege.save()
            # Set Object ID to User
            user.set_is_auhtorized(False)
            user.set_privilage(general_privilege.pk)
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
            password_in_db=user.get_user_password()
            # password invalid
            if(incoming_password!=password_in_db):
                return JsonResponse({'Message':"Wrong Password"},status=status.HTTP_400_BAD_REQUEST)
            # password valid
            else:
                print("IM D")
                token=generate_token()
                print("IM A")
                tokenlist=user.get_tokens()
                print(tokenlist)
                tokenlist.append(token)
                user.set_tokens(tokenlist)
                print("IM B")
                user.save()
                     
            
                return JsonResponse({"UserEmail":user.get_user_email(),"Token":token},status=status.HTTP_200_OK)
          
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
        token=body['Token']
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