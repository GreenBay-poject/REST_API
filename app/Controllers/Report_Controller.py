import gc
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import json
from time import time
from django.views.decorators.csrf import csrf_exempt
from app.Validator.Validator import require_validation
from app.AccessController.Rules import role_required
from app.Validator.RequiredFields import  GENERATE_DEFORESTATION_REPORT, GET_DATES, GET_IMAGE,\
    GENERATE_LAND_REPORT
from app.AccessController.Roles import ALLOWS_ALL
from app.GoogleEE.APIManager import APIManager
from datetime import datetime as dt
from app.Report_Factory.ReportFactory import ReportFactory
from app.Report_Factory.FacoryValues import DEFORESTATION_REPORT, LAND_REPORT

@csrf_exempt
@api_view(['GET'])
@require_validation(GET_DATES)
@role_required(ALLOWS_ALL)
def get_dates(request):
    try:
        # Process Data
        lattitude=float(request.GET['lattitude'])
        longitude=float(request.GET['longitude'])
        # Initialize Earth Engine
        gee_api_manager=APIManager()
        gee_api_manager.initialize()
        
        # Get Available Dates
        date_list=gee_api_manager.get_available_dates(lattitude, longitude)
        # Convert
        date_list_converted=[]
        for milli in date_list:
            date_object=dt.utcfromtimestamp(milli/1000).strftime('%Y-%m-%d')
            date_list_converted.append(date_object)
        
        
        # Return All Dates
        return JsonResponse({'All_Dates_Available':date_list_converted},status=status.HTTP_200_OK)
     
    except Exception as e:
        
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@csrf_exempt
@api_view(['GET'])
@require_validation(GET_IMAGE)
@role_required(ALLOWS_ALL)
def get_image(request):
    try:
        # Process Data
        lattitude=float(request.GET['lattitude'])
        longitude=float(request.GET['longitude'])
        date=request.GET['date']
        
        # Initialize Earth Engine
        gee_api_manager=APIManager()
        gee_api_manager.initialize()
        
        # Get Image
        image=gee_api_manager.fetch_image(lattitude, longitude, date)
        # Convert Image To Json
        image_json=image.tojson()
        
        # Return Image Urls
        return JsonResponse({'Image':image_json},status=status.HTTP_200_OK)
     
    except Exception as e:
        
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def memory_usage_psutil():
    import os
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem


@csrf_exempt
@api_view(['POST'])
@require_validation(GENERATE_LAND_REPORT)
@role_required(ALLOWS_ALL)
def generate_land_report(request):
    try:
        mem1=memory_usage_psutil()
        # Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Process Data
        url=body['url']
        print(url)
        # Generate Land Report Object
        reportObject=ReportFactory().create_report(LAND_REPORT)
        # set url to report
        reportObject.set_urls([url])
        # Generated Report
        report=reportObject.generate_report()
        print(report)
        # Clear Memory
        # del reportObject
        # Return Report
        gc.collect()
        mem2=memory_usage_psutil()
        print("Mem Consume at Begining : "+str(mem1))
        print("Mem Consume at End : "+str(mem2))
        print("Mem Consume for Call : "+str(mem2-mem1))
        return JsonResponse({'Report':report},status=status.HTTP_200_OK)
     
    except Exception as e:
         
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['POST'])
@require_validation(GENERATE_DEFORESTATION_REPORT)
@role_required(ALLOWS_ALL)
def generate_deforestation_report(request):
    try:
        mem1=memory_usage_psutil()
        # Convert request to Python Dictionary 
        body=json.loads(request.body)
        # Process Data
        url1=body['url_1']
        url2=body['url_2']
        print(url1)
        print(url2)
        # Generate Deforestation Report Object
        reportObject=ReportFactory().create_report(DEFORESTATION_REPORT)
        # set url to report
        reportObject.set_urls([url1,url2])
        # Generated Report
        report=reportObject.generate_report()
        print(report)
        # Return Report
        del reportObject
        gc.collect()
        mem2=memory_usage_psutil()
        print("Mem Consume at Begining : "+str(mem1))
        print("Mem Consume at End : "+str(mem2))
        print("Mem Consume for Call : "+str(mem2-mem1))
        return JsonResponse({'Report':report},status=status.HTTP_200_OK)
     
    except Exception as e:
        
        # Unexpected Exception Occurred
        return JsonResponse({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 