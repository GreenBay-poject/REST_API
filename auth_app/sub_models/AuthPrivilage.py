'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''

from djongo import models
from auth_app.sub_models.Posts import Posts, PostsForm
from rest_framework import serializers

class AuthPrivilage(models.Model):
    ministry=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    FeedPosts=models.ArrayField(
        model_container=Posts,
        model_form_class=PostsForm
    )
    
    
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPrivilage
        fields = ('ministry', 'position','AnswereList','FeedPosts')

    
    
