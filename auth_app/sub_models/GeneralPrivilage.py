'''
Created on Aug 3, 2021

@author: HP-PAVILLION
'''


from djongo import models
from rest_framework import serializers
from auth_app.sub_models.Questions import Questions

class GeneralPrivilage(models.Model):
    QuestionList=models.ArrayReferenceField(
        to=Questions,
        on_delete=models.CASCADE,
    )
    
    
class GeneralPrivilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralPrivilage
        fields = ('QuestionList')

    
    
