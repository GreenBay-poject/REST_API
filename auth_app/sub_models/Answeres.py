'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''
from djongo import models
from django.forms.models import ModelForm

class Answeres(models.Model):
    AnswereId=models.AutoField(primary_key=True)
    Answere=models.CharField(max_length=200)
    DatePosted=models.DateTimeField()
# class AnsweresForm(ModelForm):
# 
#     class Meta:
#         model = Answeres
#         fields = (
#             'AnswereId','Answere','DatePosted'
#         )