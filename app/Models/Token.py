from djongo import models
from django.forms import ModelForm

class Token(models.Model):
    
    value=models.CharField(max_length=200)
    generated_time=models.DateTimeField()
    isvalid=models.BooleanField()
    def get_value(self):
        return self.value

    def get_generated_time(self):
        return self.generated_time

    def get_isvalid(self):
        return self.isvalid

    def set_value(self, value):
        self.value = value

    def set_generated_time(self, value):
        self.generated_time = value

    def set_isvalid(self, value):
        self.isvalid = value
   
    class Meta:
        abstract = True

class TokenForm(ModelForm):

    class Meta:
        model = Token
        fields = (
            'value','generated_time','isvalid'
        )