'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''
from djongo import models
from auth_app.sub_models.Answeres import Answeres

class Questions(models.Model):
    QuestionId=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=200)
    Question=models.CharField(max_length=200)
    DatePosted=models.DateTimeField()
    AnsweresList=models.ArrayReferenceField(
        to=Answeres,
        on_delete=models.CASCADE,
    )
    