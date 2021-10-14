from django.conf.urls import url 
from app.Controllers import Auth_Controller, Feed_Controller
urlpatterns = [ 
    url(r'^add_post$', Feed_Controller.add_post),
    url(r'^view_my_posts$', Feed_Controller.view_my_posts),
    url(r'^delete_post$', Feed_Controller.delete_post),
    url(r'^view_posts$', Feed_Controller.view_posts),
]