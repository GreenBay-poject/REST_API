from django.conf.urls import url 
from app.Controllers import Report_Controller
urlpatterns = [ 
    url(r'^get_dates', Report_Controller.get_dates)
]