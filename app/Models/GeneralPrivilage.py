from djongo import models
from app.Models.Questions import Questions

class  GeneralPrivilage(models.Model):
        
    QuestionList=models.CharField(
        to=Questions,
        on_delete=models.CASCADE,
    )
    
    def get_question_list(self):
        return self.QuestionList

    def set_question_list(self, value):
        self.QuestionList = value   
