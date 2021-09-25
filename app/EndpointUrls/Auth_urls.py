from django.conf.urls import url 
from app.Controllers import Auth_Controller
urlpatterns = [ 
    url(r'^get_user_info', Auth_Controller.get_user_details),
    url(r'^register$', Auth_Controller.registeruser),
    url(r'^authregister$', Auth_Controller.register_auth_user),
    url(r'^login$', Auth_Controller.loginuser),
    url(r'^logout$', Auth_Controller.logout),
    url(r'^forget$', Auth_Controller.forget_password),
    url(r'^changepassword$', Auth_Controller.change_password),
]