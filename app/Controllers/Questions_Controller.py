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
@role_required(ALLOWS_GENERAL_USERS_ONLY)
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
        print('***********************')
        print(question_list)
        # if question_list.count() < 1:
        question = Questions()
        question.set_title(body['title'])
        question.set_question(body['question'])
        question.set_date_posted(datetime.now())
        question.save()
        question_ref = question.pk
        print(question.get_title())
        print(question.pk)
        question_list.append(question_ref)
        print(question_list)
        privilege.set_question_list(question_list)
        # print("A")
        # print(privilege.get_question_list)
        # # Save privilege list
        privilege.save()
        # # Notify users when add posts

        return JsonResponse({'All Questions By The user':privilege.get_question_list()}, status=status.HTTP_200_OK)
     
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
            user_data = {}
            # set email
            user_data['email'] = user.get_user_email()
            print(user.get_user_email())
            # get privilege id
            privilege_id = user.get_privilage()
            # Get Privilege Object
            privilege = GeneralPrivilage.objects.filter(id=privilege_id).first();
            # Get Posts list
            questions_list = privilege.get_question_list()
            print(questions_list)
            if len(questions_list) < 1:
                continue
            questionObj = []
            for questionref in questions_list:
                question=Questions.objects.filter(id=questionref).first();
                Question={}
                Question['title']=question.get_title()
                Question['question']=question.get_question()
                Question['dateposted']=question.get_date_posted()
                Question['q_id'] = question.pk
                Question['answer'] = question.get_answeres_list()
                questionObj.append(Question)
            user_data['questions'] = questionObj
            response.append(user_data)

        # Send response
        return JsonResponse({'ALL_QUESTIONS': response}, status=status.HTTP_200_OK)

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
        privilege = GeneralPrivilage.objects.filter(id=privilege_id).first();
        # Get Posts list
        question_list = privilege.get_question_list()
        print(question_list)
        # Delete Post From List
        removed_question = None
        i = 0
        for question in question_list:
            if question['q_id'] == body['Question_id']:
                removed_question = question_list.pop(i)
            i = i + 1
        #print(post_list)
        # Update post list
        privilege.set_question_list(question_list)        
        # if no error save
        privilege.save()
        # Send response
        return JsonResponse({'Deleted Question ID':removed_question, 'All Posts By The user':question_list}, status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@require_validation(ANSWER_QUESTIONS)
@role_required(ALLOWS_MINISTRY_USERS_ONLY)
def answer_questions(request):
    try:
        # Convert request to Python Dictionary
        body = json.loads(request.body)
        # Get users list
        user_list = Users.objects.filter(UserEmail=body['email']);
        # Get the user object
        user = user_list.first()
        question = Questions.objects.filter(id=body['question_id']).first();

        answer_list=question.get_answeres_list()

        post_dictionary = {'post_id': int(time() * 1000), 'Answere': body['answer'], 'AuthorsID': user.pk, 'DatePosted': datetime.now()}

        answer_list.append(post_dictionary)

        question.set_answeres_list(answer_list)


            
        # Send response
        return JsonResponse({'ALL_POSTS':[]}, status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
