from djongo import models
from django.forms.models import ModelForm

class Answeres(models.Model):
    
    Answere=models.CharField(max_length=2000)
    DatePosted=models.DateTimeField()
    AuthorsID=models.CharField(max_length=500)
    
    def get_answere(self):
        return self.Answere

    def get_date_posted(self):
        return self.DatePosted

    def get_authors_id(self):
        return self.AuthorsID

    def set_answere(self, value):
        self.Answere = value

    def set_date_posted(self, value):
        self.DatePosted = value

    def set_authors_id(self, value):
        self.AuthorsID = value
      
    class Meta:
        abstract=True

class AnsweresForm(ModelForm):
 
        class Meta:
            model = Answeres
            fields = (
                'Answere','DatePosted','AuthorsID'
            )