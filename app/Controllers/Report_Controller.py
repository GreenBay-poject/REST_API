from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
from time import time
from django.views.decorators.csrf import csrf_exempt
from app.Validator.Validator import require_validation
from app.AccessController.Rules import role_required
from app.Validator.RequiredFields import GET_DATES
from app.AccessController.Roles import ALLOWS_ALL
from app.GoogleEE.APIManager import APIManager

@csrf_exempt
@api_view(['GET'])
@require_validation(GET_DATES)
@role_required(ALLOWS_ALL)
def get_dates(request,lattitude,longitude):
    try:
        
        # Initialize Earth Engine
        gee_api_manager=APIManager()
        gee_api_manager.initialize()
        
        # Get Available Dates
        date_list=gee_api_manager.get_available_dates(lattitude, longitude)
        
        # Return All Dates
        return JsonResponse({'All Dates Available':date_list},status=status.HTTP_200_OK)
     
    except Exception as e:
        
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

