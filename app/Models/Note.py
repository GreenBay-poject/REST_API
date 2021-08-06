from djongo import models
from django.forms import ModelForm

class Note(models.Model):

    lat=models.FloatField()
    lon=models.FloatField()
    text=models.CharField(max_length=200)
    
    def get_lat(self):
        return self.__lat

    def get_lon(self):
        return self.__lon

    def get_text(self):
        return self.__text

    def set_lat(self, value):
        self.__lat = value

    def set_lon(self, value):
        self.__lon = value

    def set_text(self, value):
        self.__text = value

    class Meta:
        abstract = True

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = (
            'lat','lon','text'
        )