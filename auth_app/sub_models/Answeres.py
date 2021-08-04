'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''
from djongo import models
from django.forms.models import ModelForm

class Answeres(models.Model):
    Answere=models.CharField(max_length=2000)
    DatePosted=models.DateTimeField()
    AuthorsID=models.CharField(max_length=500)
    class Meta:
        abstract=True
class AnsweresForm(ModelForm):
 
        class Meta:
            model = Answeres
            fields = (
                'Answere','DatePosted','AuthorsID'
             
            )