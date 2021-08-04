'''
Created on Aug 3, 2021

@author: HP-PAVILLION
'''


from djongo import models
from auth_app.sub_models.Questions import Questions

class GeneralPrivilage(models.Model):
    QuestionList=models.ArrayReferenceField(
        to=Questions,
        on_delete=models.CASCADE,
    )

    
