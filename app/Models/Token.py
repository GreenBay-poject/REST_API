from djongo import models
from django.forms import ModelForm

class Token(models.Model):
    
    value=models.CharField(max_length=200)
    generated_time=models.DateTimeField()
    isvalid=models.BooleanField()
    def get_value(self):
        return self.__value

    def get_generated_time(self):
        return self.__generated_time

    def get_isvalid(self):
        return self.__isvalid

    def set_value(self, value):
        self.__value = value

    def set_generated_time(self, value):
        self.__generated_time = value

    def set_isvalid(self, value):
        self.__isvalid = value
   
    class Meta:
        abstract = True

class TokenForm(ModelForm):

    class Meta:
        model = Token
        fields = (
            'value','generated_time','isvalid'
        )