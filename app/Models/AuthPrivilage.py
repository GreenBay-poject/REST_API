from djongo import models
from app.Models.Posts import Posts, PostsForm

class AuthPrivilage(models.Model):
    
    ministry_refrence=models.CharField(max_length=500)
    position=models.CharField(max_length=200)
    FeedPosts=models.ArrayField(
        model_container=Posts,
        model_form_class=PostsForm
    )

    def get_ministry_refrence(self):
        return self.__ministry_refrence

    def get_position(self):
        return self.__position

    def get_feed_posts(self):
        return self.__FeedPosts

    def set_ministry_refrence(self, value):
        self.__ministry_refrence = value

    def set_position(self, value):
        self.__position = value

    def set_feed_posts(self, value):
        self.__FeedPosts = value