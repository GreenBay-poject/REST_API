from back_end_rest_api.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def send_answer_added_email(send_to,question_title,question_description,answer,answer_by): 
    print(send_to)
    print(question_title)
    print(question_description)
    print(answer)
    print(answer_by)

    subject = 'Your Question Has Answered ...'
    message1 = 'Question Title :\n'+question_title+'\n'
    message2 = 'Question Description :\n'+question_description+'\n'
    message3 = 'Answer :\n'+answer+'\n'
    message4 = 'Answered By :\n'+answer_by+'\n'
 
    complete_mail=message1+message2+message3+message4

    print(complete_mail)

    send_mail(subject,complete_mail, EMAIL_HOST_USER, [send_to], fail_silently = True)