from django.conf.urls import url 
from app.Controllers import Auth_Controller, Feed_Controller, Note_Controller
urlpatterns = [ 
    url(r'^add_note$', Note_Controller.add_note),
]