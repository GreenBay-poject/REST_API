from django.conf.urls import url 
from app.Controllers import Auth_Controller, Questions_Controller
urlpatterns = [ 
    url(r'^add_question$', Questions_Controller.add_questions),
    url(r'^view_questions$', Questions_Controller.view_questions),
    url(r'^delete_questions$', Questions_Controller.delete_questions),
    url(r'^answer_questions$', Questions_Controller.answer_questions),   
]