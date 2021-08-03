'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''
from djongo import models

from django.forms import ModelForm

class Posts(models.Model):
    Title=models.CharField(max_length=200)
    Image=models.CharField(max_length=1000)
    Description=models.CharField(max_length=200)
    DatePosted=models.DateTimeField()
    class Meta:
        abstract = True

class PostsForm(ModelForm):

    class Meta:
        model = Posts
        fields = (
            'Title','Image','Description','DatePosted'
        )