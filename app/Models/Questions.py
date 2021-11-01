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
        return self.Title

    def get_question(self):
        return self.Question

    def get_date_posted(self):
        return self.DatePosted

    def get_answeres_list(self):
        return self.AnsweresList

    def set_title(self, value):
        self.Title = value

    def set_question(self, value):
        self.Question = value

    def set_date_posted(self, value):
        self.DatePosted = value

    def set_answeres_list(self, value):
        self.AnsweresList = value  