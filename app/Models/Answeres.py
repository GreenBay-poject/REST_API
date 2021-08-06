from djongo import models
from django.forms.models import ModelForm

class Answeres(models.Model):
    
    Answere=models.CharField(max_length=2000)
    DatePosted=models.DateTimeField()
    AuthorsID=models.CharField(max_length=500)
    
    def get_answere(self):
        return self.__Answere

    def get_date_posted(self):
        return self.__DatePosted

    def get_authors_id(self):
        return self.__AuthorsID

    def set_answere(self, value):
        self.__Answere = value

    def set_date_posted(self, value):
        self.__DatePosted = value

    def set_authors_id(self, value):
        self.__AuthorsID = value
      
    class Meta:
        abstract=True

class AnsweresForm(ModelForm):
 
        class Meta:
            model = Answeres
            fields = (
                'Answere','DatePosted','AuthorsID'
            )