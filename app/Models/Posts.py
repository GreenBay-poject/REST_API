from djongo import models
from django.forms import ModelForm

class Posts(models.Model):
    
    Title=models.CharField(max_length=200)
    Image=models.CharField(max_length=1000)
    Description=models.CharField(max_length=200)
    DatePosted=models.DateTimeField()

    def get_title(self):
        return self.__Title

    def get_image(self):
        return self.__Image

    def get_description(self):
        return self.__Description

    def get_date_posted(self):
        return self.__DatePosted

    def set_title(self, value):
        self.__Title = value

    def set_image(self, value):
        self.__Image = value

    def set_description(self, value):
        self.__Description = value

    def set_date_posted(self, value):
        self.__DatePosted = value
    
    class Meta:
        abstract = True

class PostsForm(ModelForm):

    class Meta:
        model = Posts
        fields = (
            'Title','Image','Description','DatePosted'
        )