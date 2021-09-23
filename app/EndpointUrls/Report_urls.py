from django.conf.urls import url 
from app.Controllers import Report_Controller
urlpatterns = [ 
    url(r'^get_dates', Report_Controller.get_dates),
    url(r'^get_image', Report_Controller.get_image),
    url(r'^generate_land_report', Report_Controller.generate_land_report),
    url(r'^generate_deforestation_report', Report_Controller.generate_deforestation_report)
]