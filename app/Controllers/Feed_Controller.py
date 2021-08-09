from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
from app.Models.Users import Users
from datetime import datetime
import hashlib
from django.views.decorators.csrf import csrf_exempt
from app.Validator.Validator import require_validation
from app.Validator.RequiredFields import *
from app.AccessController.Rules import role_required
from app.AccessController.Roles import *
from app.Helpers.Auth_Helper import generate_password, send_password_to,\
    generate_token
from app.Models.GeneralPrivilage import GeneralPrivilage
from back_end_rest_api.settings import SECRET_CODE
from app.Models.AuthPrivilage import AuthPrivilage
from app.Models.Ministry import Ministry

@csrf_exempt
@api_view(['POST'])
@require_validation(ADD_POST)
@role_required(ALLOWS_MINISTRY_USERS_ONLY)
def add_post(request):
    try:
        # Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Get users list
        user_list=Users.objects.filter(UserEmail=body['email']);
        # Get the user object
        user=user_list.first()
        # get privilege id
        privilege_id=user.get_privilage()
        # Get Privilege Object
        privilege=AuthPrivilage.objects.filter(id=privilege_id).first();
        # Get Posts list
        post_list=privilege.get_feed_posts()
        # Add a post to post_list
        post_list.add({'Title':body['title'],
                       'Image':body['image_url'],
                       'Description':body['description'],
                       'DatePosted':datetime.datetime.now().timestamp(),                    
                       })
        # Update post list
        privilege.set_feed_posts(post_list)
        # Save privilege list
        privilege.save()
        # Send response
        return JsonResponse({'All Posts':privilege.get_feed_posts()},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


