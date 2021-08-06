from django.conf.urls import url 
from app.Controllers import Auth_Controller
urlpatterns = [ 
    url(r'^register$', Auth_Controller.registeruser),
   # url(r'^login$', Auth_Controller.loginuser),
   # url(r'^logout$', Auth_Controller.logout),
   # url(r'^forget$', Auth_Controller.forget_password),
]