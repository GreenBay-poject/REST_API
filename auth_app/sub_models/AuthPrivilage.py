'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''

from djongo import models
from django.forms import ModelForm
from auth_app.sub_models.Answeres import Answeres
from auth_app.sub_models.Posts import Posts
from rest_framework import serializers

class AuthPrivilage(models.Model):
    ministry=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    
    AnswereList=models.ArrayReferenceField(
        to=Answeres,
        on_delete=models.CASCADE,
    )
    FeedPosts=models.ArrayReferenceField(
        to=Posts,
        on_delete=models.CASCADE,
    )
    
    
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPrivilage
        fields = ('ministry', 'position','AnswereList','FeedPosts')

    
    
