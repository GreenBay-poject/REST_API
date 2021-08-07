from random import choice
from string import ascii_uppercase
from back_end_rest_api.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from _datetime import datetime

def generate_password():
    return ''.join(choice(ascii_uppercase) for i in range(12))

def send_password_to(user,password): 
    subject = 'Welcome to GreenBay'
    message1 = 'Congratulations! You are now member of GreenBay community, Here is your credintials for future logins\n\nEmail : {}\nPassword : {}\n\n'.format(user.UserEmail,password)
    message2 = 'Note : You can change password using account page'
    recepient = str(user.UserEmail)
    send_mail(subject,message1+message2, EMAIL_HOST_USER, [recepient], fail_silently = False)
    
def generate_token():
    token={"value":None,"generated_time":None,"isvalid":None}
    token['value']= ''.join(choice(ascii_uppercase) for i in range(25))
    token['generated_time']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    token['isvalid']=True
    return token
