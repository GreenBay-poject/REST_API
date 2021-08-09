from djongo import models
from django.forms import ModelForm

class Note(models.Model):

    lat=models.FloatField()
    lon=models.FloatField()
    text=models.CharField(max_length=200)
    
    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def get_text(self):
        return self.text

    def set_lat(self, value):
        self.lat = value

    def set_lon(self, value):
        self.lon = value

    def set_text(self, value):
        self.text = value

    class Meta:
        abstract = True

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = (
            'lat','lon','text'
        )