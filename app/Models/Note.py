from djongo import models
from django.forms import ModelForm
from django.db.models.fields import AutoField

class Note(models.Model):

    note_id=models.IntegerField()
    lat=models.FloatField()
    lon=models.FloatField()
    text=models.CharField(max_length=200)
    
    
    def get_note_id(self):
        return self.note_id

    def set_note_id(self, value):
        self.note_id = value
    
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
            'note_id','lat','lon','text'
        )