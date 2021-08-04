'''
Created on Jul 25, 2021

@author: HP-PAVILLION
'''

from djongo import models
from auth_app.sub_models.Posts import Posts, PostsForm

class AuthPrivilage(models.Model):
    ministry_refrence=models.CharField(max_length=500)
    position=models.CharField(max_length=200)
    FeedPosts=models.ArrayField(
        model_container=Posts,
        model_form_class=PostsForm
    )
    

