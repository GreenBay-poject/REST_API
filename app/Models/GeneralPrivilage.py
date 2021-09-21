from app.Models.ValueQID import ValueQID, ValueQIDForm
from django.forms import ModelForm
from djongo import models

class  GeneralPrivilage(models.Model):
        
    QuestionList=models.JSONField()
    
    def get_question_list(self):
        return self.QuestionList

    def set_question_list(self, value):
        self.QuestionList = value   


