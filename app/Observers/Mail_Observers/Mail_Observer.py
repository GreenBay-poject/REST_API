from django.core.mail import send_mail
from back_end_rest_api.settings import EMAIL_HOST_USER
from app.Observers.Observer import observer

class Mail_Observer(observer):
    
    def __init__(self,mail_list):
        self.mail_list=mail_list
    
    def update(self,dictionary):
        print("sending:"+str(dictionary))
        print("to:"+str(self.mail_list))
        subject = dictionary['Title']
        message1 = dictionary['Description'] 
        send_mail(subject,message1, EMAIL_HOST_USER,self.mail_list, fail_silently = True)