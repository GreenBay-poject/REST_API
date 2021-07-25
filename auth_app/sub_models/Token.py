'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''
from djongo import models
from django.forms import ModelForm

class Token(models.Model):
    value=models.CharField(max_length=200)
    generated_time=models.DateTimeField()
    isvalid=models.BooleanField()
    class Meta:
        abstract = True

class TokenForm(ModelForm):

    class Meta:
        model = Token
        fields = (
            'value','generated_time','isvalid'
        )