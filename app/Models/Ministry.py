from djongo import models

class Ministry(models.Model):
    
    ministry_name=models.CharField(max_length=200)

    def get_ministry_name(self):
        return self.ministry_name

    def set_ministry_name(self, value):
        self.ministry_name = value 