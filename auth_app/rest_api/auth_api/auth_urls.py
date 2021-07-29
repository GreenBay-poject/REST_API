'''
Created on Jul 27, 2021

@author: HP-PAVILLION
'''
from django.conf.urls import url 
from auth_app.rest_api.auth_api import endpoints
urlpatterns = [ 
    url(r'^register$', endpoints.registeruser),
    url(r'^login$', endpoints.loginuser),
    url(r'^logout$', endpoints.logout),
]