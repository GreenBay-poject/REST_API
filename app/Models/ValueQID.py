
from django.forms import ModelForm
from djongo import models

class ValueQID(models.Model):
    key = models.CharField(max_length=100)

    class Meta:
        abstract = True

class ValueQIDForm(ModelForm):
    class Meta:
        model = ValueQID
        fields = ('key',)