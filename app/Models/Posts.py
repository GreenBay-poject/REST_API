from djongo import models
from django.forms import ModelForm

class Posts(models.Model):

    post_id=models.IntegerField()
    Title=models.CharField(max_length=200)
    Image=models.CharField(max_length=1000)
    Description=models.CharField(max_length=200)
    DatePosted=models.DateTimeField()
    
    def get_post_id(self):
        return self.post_id


    def set_post_id(self, value):
        self.post_id = value

    def get_title(self):
        return self.Title

    def get_image(self):
        return self.Image

    def get_description(self):
        return self.Description

    def get_date_posted(self):
        return self.DatePosted

    def set_title(self, value):
        self.Title = value

    def set_image(self, value):
        self.Image = value

    def set_description(self, value):
        self.Description = value

    def set_date_posted(self, value):
        self.DatePosted = value
    
    class Meta:
        abstract = True
    
class PostsForm(ModelForm):

    class Meta:
        model = Posts
        fields = (
           'post_id','Title','Image','Description','DatePosted'
        )