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
from time import time

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
        print("::")
        # Get Privilege Object
        privilege=AuthPrivilage.objects.filter(id=privilege_id).first();
        # Get Posts list
        post_list=privilege.get_feed_posts()
        # Add a post to post_list
        print("::")
        post_dictionary={'post_id':int(time()*1000),'Title':body['title'],'Image':body['image_url'],'Description':body['description'],'DatePosted':datetime.now()}
        print("::")
        post_list.append(post_dictionary)
        print(post_list)
        # Update post list
        privilege.set_feed_posts(post_list)
        print("A")
        # Save privilege list
        privilege.save()
        # Notify users when add posts
        try:
            user.notifyall(post_dictionary)
        
        # Send response
        return JsonResponse({'All Posts By The user':privilege.get_feed_posts()},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        removed_post=None
        for post in post_list:
            i=0
            if post['post_id']==body['post_id']:
                removed_post=post_list.pop(i)
            i=i+1
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



