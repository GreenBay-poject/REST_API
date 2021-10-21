from django.http.response import JsonResponse
from rest_framework import status
import json


def require_validation(field_list):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            #Read Body
            body={}
            if request.method=='POST':
                body=json.loads(request.body)
            if request.method=='GET':
                body=request.query_params
            valid=True # Consider as Valid
            # Iterate and Check For Existence
            for field in field_list:
                if field not in body.keys():
                    valid=False
                    break
            # All FIELDS AVAILABLE
            if(valid):
                return view_func(request, *args, **kwargs)
            else: # MISSING FIELDS
                return JsonResponse({"Message":"REQUIRE FIELDS NOT FOUND"},status=status.HTTP_400_BAD_REQUEST)
            
        return wrap
    return decorator
