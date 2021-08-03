'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''
from djongo import models
from auth_app.sub_models.Note import Note, NoteForm
from auth_app.sub_models.Token import Token, TokenForm

class Users(models.Model):
    UserName=models.CharField(max_length=50)
    UserEmail=models.EmailField(max_length=50)
    UserPassword=models.CharField(max_length=50)
    UserAge=models.IntegerField()
    Gender=models.CharField(max_length=200)
    PostalCode=models.IntegerField()
    DateRegistered=models.DateTimeField()
    
    Notes=models.ArrayField(
        model_container=Note,
        model_form_class=NoteForm
    )
    Tokens=models.ArrayField(
        model_container=Token,
        model_form_class=TokenForm
    )
    Privilage=models.CharField(max_length=500)
    