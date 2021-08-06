from djongo import models
from app.Models.Answeres import Answeres, AnsweresForm

class Questions(models.Model):
    
    Title=models.CharField(max_length=200)
    Question=models.CharField(max_length=200)
    DatePosted=models.DateTimeField()
    AnsweresList=models.ArrayField(
        model_container=Answeres,
        model_form_class=AnsweresForm
    )

    def get_title(self):
        return self.__Title

    def get_question(self):
        return self.__Question

    def get_date_posted(self):
        return self.__DatePosted

    def get_answeres_list(self):
        return self.__AnsweresList

    def set_title(self, value):
        self.__Title = value

    def set_question(self, value):
        self.__Question = value

    def set_date_posted(self, value):
        self.__DatePosted = value

    def set_answeres_list(self, value):
        self.__AnsweresList = value  