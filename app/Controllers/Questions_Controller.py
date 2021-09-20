from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
from app.Models.Users import Users
from app.Models.Questions import Questions
from app.Models.Answeres import Answeres
from datetime import datetime
import hashlib
from django.views.decorators.csrf import csrf_exempt
from app.Validator.Validator import require_validation
from app.Validator.RequiredFields import *
from app.AccessController.Rules import role_required
from app.AccessController.Roles import *
from app.Helpers.Auth_Helper import generate_password, send_password_to, \
    generate_token
from app.Models.GeneralPrivilage import GeneralPrivilage
from back_end_rest_api.settings import SECRET_CODE
from app.Models.AuthPrivilage import AuthPrivilage
from app.Models.Ministry import Ministry
from time import time
from app.Observers.Mail_Observers.Mail_Observer import Mail_Observer
from app.Observers.Posts_observable.Post_Observable import Post_Observable
from app.Models.Questions import Questions


@csrf_exempt
@api_view(['POST'])
@require_validation(ADD_QUESTIONS)
@role_required(ALLOWS_REGULAR_AND_MINISTRY_USERS)
def add_questions(request):
    try:
        # Convert request to Python Dictionary 
        body = json.loads(request.body)
        # Get users list
        user_list = Users.objects.filter(UserEmail=body['email']);
        # Get the user object
        user = user_list.first()
        # get privilege id
        privilege_id = user.get_privilage()
        # Get Privilege Object
        privilege = GeneralPrivilage.objects.filter(id=privilege_id).first();
        # Get Posts list
        question_list = privilege.get_question_list()
        print(question_list.count())
        question_ref = -1
        if question_list.count() < 1:
            question = Questions()
            question.set_title(body['title'])
            question.set_question(body['question'])
            question.set_date_posted(datetime.now())
            question.save()
            question_ref = question.pk
            print(question.get_title())
            print(question.pk)
        else:
            question_ref = question_list.first().pk
        print(question_ref)
        print(question_list)
        question_list=[]
        question_list.append(question_ref)
        print(question_list)
        privilege.set_question_list(question_list)
        print("A")
        print(privilege.get_question_list)
        # Save privilege list
        privilege.save()
        # Notify users when add posts

        return JsonResponse({'All Questions By The user':[]}, status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@require_validation(VIEW_QUESTIONS)
@role_required(ALLOWS_REGULAR_AND_MINISTRY_USERS)
def view_questions(request):
    try:
        print("A")
        # Get users list
        user_list = Users.objects.all();
        # response
        print("A")
        print(len(user_list))
        print("B")
        response = []
        # iterate through user list
        for user in user_list:
            if not user.get_is_auhtorized():
                continue
            user_data = {}
            # set email
            user_data['email'] = user.get_user_email()
            print("hiiii isuruu")
            # get privilege id
            privilege_id = user.get_privilage()
            # Get Privilege Object
            privilege = GeneralPrivilage.objects.filter(id=privilege_id).first();
            # Get Posts list
            questions_list = privilege.get_question_list()
            print(questions_list.count())
            if questions_list.count() > 0:
                question=Questions.objects.filter(id=questions_list[0]).first().get_title()
                print("hiii")
                print(question)
                user_data['Title']=question.Title
            response.append(user_data)

        # Send response
        return JsonResponse({'ALL_POSTS': response}, status=status.HTTP_200_OK)

    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@require_validation(DELETE_QUESTIONS)
@role_required(ALLOWS_MINISTRY_USERS_ONLY)
def delete_questions(request):
    try:
        # Convert request to Python Dictionary 
        body = json.loads(request.body)
        # Get users list
        user_list = Users.objects.filter(UserEmail=body['email']);
        # Get the user object
        user = user_list.first()
        # get privilege id
        privilege_id = user.get_privilage()
        # Get Privilege Object
        privilege = AuthPrivilage.objects.filter(id=privilege_id).first();
        # Get Posts list
        post_list = privilege.get_feed_posts()
        print(post_list)
        # Delete Post From List
        removed_post = None
        for post in post_list:
            i = 0
            if post['post_id'] == body['post_id']:
                removed_post = post_list.pop(i)
            i = i + 1
        print(post_list)
        # Update post list
        privilege.set_feed_posts(post_list)
        print("A")
        # Save privilege list
        privilege.save()
        # Send response
        return JsonResponse({'Deleted Post':removed_post, 'All Posts By The user':privilege.get_feed_posts()}, status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET'])
@require_validation(ANSWER_QUESTIONS)
@role_required(ALLOWS_MINISTRY_USERS_ONLY)
def answer_question(request):
    try:
        print("A")
        # Get users list
        user_list = Users.objects.all();
        # response
        print("A")
        print(len(user_list))
        print("B")
        response = []
        # iterate through user list
        for user in user_list:
            if not user.get_is_auhtorized():
                continue
            user_data = {}
            # set email
            user_data['email'] = user.get_user_email()
            # get privilege id
            privilege_id = user.get_privilage()
            # Get Privilege Object
            privilege = AuthPrivilage.objects.filter(id=privilege_id).first();
            # Get Posts list
            post_list = privilege.get_feed_posts()
            # set post list
            user_data['posts'] = post_list
            # get ministry id
            ministry_id = privilege.get_ministry_refrence()
            # get ministry name
            ministry_name = Ministry.objects.filter(id=ministry_id).first().get_ministry_name()
            # set ministry name
            user_data['ministry_name'] = ministry_name
            # Add data to response
            response.append(user_data)
            
        # Send response
        return JsonResponse({'ALL_POSTS':response}, status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

