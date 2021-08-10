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
@require_validation(ADD_NOTE)
@role_required(ALLOWS_REGULAR_AND_MINISTRY_USERS)
def add_note(request):
    try:
        # Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Get users list
        user_list=Users.objects.filter(UserEmail=body['email']);
        # Get the user object
        user=user_list.first()
        # Get Note List
        note_list=user.get_notes()
        # Add Note To List
        note_list.append({
            "lat":body['lat'],
            "lon":body['lon'],
            "text":body['text']
            })
        # Set Note List
        user.set_notes(note_list)
        # Save User
        user.save()
        # Return All Notes
        return JsonResponse({'All Notes By The user':user.get_notes()},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


'''
@csrf_exempt
@api_view(['POST'])
@require_validation(VIEW_MY_POSTS)
@role_required(ALLOWS_MINISTRY_USERS_ONLY)
def view_my_posts(request):
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
        # Send response
        return JsonResponse({'All Posts By The user':post_list},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@require_validation(DELETE_MY_POSTS)
@role_required(ALLOWS_MINISTRY_USERS_ONLY)
def delete_post(request):
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
        print(post_list)
        # Delete Post From List
        index=body['post_index']
        removed_post=post_list.pop(index)
        print(post_list)
        # Update post list
        privilege.set_feed_posts(post_list)
        print("A")
        # Save privilege list
        privilege.save()
        # Send response
        return JsonResponse({'Deleted Post':removed_post,'All Posts By The user':privilege.get_feed_posts()},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['GET'])
@require_validation(VIEW_ALL_POSTS)
@role_required(ALLOWS_ALL)
def view_posts(request):
    try:
        print("A")
        # Get users list
        user_list=Users.objects.all();
        # response
        print("A")
        print(len(user_list))
        print("B")
        response=[]
        # iterate through user list
        for user in user_list:
            if not user.get_is_auhtorized():
                continue
            user_data={}
            # set email
            user_data['email']=user.get_user_email()
            # get privilege id
            privilege_id=user.get_privilage()
            # Get Privilege Object
            privilege=AuthPrivilage.objects.filter(id=privilege_id).first();
            # Get Posts list
            post_list=privilege.get_feed_posts()
            # set post list
            user_data['posts']=post_list
            # get ministry id
            ministry_id=privilege.get_ministry_refrence()
            # get ministry name
            ministry_name=Ministry.objects.filter(id=ministry_id).first().get_ministry_name()
            # set ministry name
            user_data['ministry_name']=ministry_name
            # Add data to response
            response.append(user_data)
        
        # Send response
        return JsonResponse({'ALL POSTS':response},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



'''