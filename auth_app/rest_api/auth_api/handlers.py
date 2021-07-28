'''
Created on Jul 27, 2021

@author: HP-PAVILLION
'''

from random import choice
from string import ascii_uppercase
from back_end_rest_api.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.core.mail.message import EmailMessage



def generate_password():
    return ''.join(choice(ascii_uppercase) for i in range(12))

def send_password_to(user,password):
    print("Passed Me")
    message = get_template('mail.html').render(Context({
        'email': user.UserEmail,
        'password': password
    }))
    print("ADA")
    mail = EmailMessage(
        subject="Registered to Green Bay ",
        body=message,
        from_email="admin@greenbay.com",
        to=[user.UserEmail],
        reply_to=['admin@greenbay.com'],
        fail_silently = False
    )
    mail.content_subtype = "html"
    mail.send()