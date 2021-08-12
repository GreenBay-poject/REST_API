from django.conf.urls import url 
from app.Controllers import Auth_Controller, Feed_Controller, Note_Controller
urlpatterns = [ 
    url(r'^add_note$', Note_Controller.add_note),
    url(r'^view_my_notes$', Note_Controller.view_my_notes),
    url(r'^delete_note$', Note_Controller.delete_note),
    url(r'^get_public_note$', Note_Controller.view_public_notes),
]
'''
(x|xy)*b(a|b)*
xxb
xyb
xbb
xba
baa
bab
bba
bbb

'''