from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
from time import time
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
            "note_id":int(time()*1000),
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



@csrf_exempt
@api_view(['POST'])
@require_validation(VIEW_MY_NOTES)
@role_required(ALLOWS_REGULAR_AND_MINISTRY_USERS)
def view_my_notes(request):
    try:
        # Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Get users list
        user_list=Users.objects.filter(UserEmail=body['email']);
        # Get the user object
        user=user_list.first()
        # Get Note List
        note_list=user.get_notes()
        # Return All Notes
        return JsonResponse({'All Notes By The user':note_list},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@csrf_exempt
@api_view(['POST'])
@require_validation(DELETE_MY_NOTE)
@role_required(ALLOWS_REGULAR_AND_MINISTRY_USERS)
def delete_note(request):
    try:
        # Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Get users list
        user_list=Users.objects.filter(UserEmail=body['email']);
        # Get the user object
        user=user_list.first()
        # Get Note List
        note_list=user.get_notes()
        # Delete Note From List
        deleted_note=None
        for note in note_list:
            i=0
            if note['note_id']==body['note_id']:
                deleted_note=note_list.pop(i)
            i=i+1
        
        # Set Note List
        user.set_notes(note_list)
        # Save User
        user.save()
        # Return All Notes
        return JsonResponse({'Deleted Note':deleted_note,'All Notes By The user':user.get_notes()},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET'])
@require_validation(VIEW_PUBLIC_NOTES)
@role_required(ALLOWS_ALL)
def view_public_notes(request):
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
            # A filter for public notes
            if not user.get_is_auhtorized():
                continue
            user_data={}
            # set email
            user_data['email']=user.get_user_email()
            # get privilege id
            privilege_id=user.get_privilage()
            # Get Privilege Object
            privilege=AuthPrivilage.objects.filter(id=privilege_id).first();
            # Get Notes list
            note_list=user.get_notes()
            # set note list
            user_data['notes']=note_list
            # get ministry id
            ministry_id=privilege.get_ministry_refrence()
            # get ministry name
            ministry_name=Ministry.objects.filter(id=ministry_id).first().get_ministry_name()
            # set ministry name
            user_data['ministry_name']=ministry_name
            # Add data to response
            response.append(user_data)
        
        # Send response
        return JsonResponse({'ALL_NOTES':response},status=status.HTTP_200_OK)
     
    except Exception as e:
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

