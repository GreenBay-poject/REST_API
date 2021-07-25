'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''
from djongo import models
from django.forms import ModelForm

class Note(models.Model):
    lat=models.FloatField()
    lon=models.FloatField()
    text=models.CharField(max_length=200)
    class Meta:
        abstract = True

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = (
            'lat','lon','text'
        )