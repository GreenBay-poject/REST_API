from djongo import models
from app.Models.Note import Note, NoteForm
from app.Models.Token import Token, TokenForm

class Users(models.Model):
    
    UserName=models.CharField(max_length=50)
    UserEmail=models.EmailField(max_length=50)
    UserPassword=models.CharField(max_length=50)
    UserAge=models.IntegerField()
    IsAuhtorized=models.BooleanField()
    Gender=models.CharField(max_length=200)
    Address=models.CharField(max_length=500)
    PostalCode=models.IntegerField()
    DateRegistered=models.DateTimeField()
    Notes=models.ArrayField(
        model_container=Note,
        model_form_class=NoteForm
    )
    Tokens=models.ArrayField(
        model_container=Token,
        model_form_class=TokenForm
    )
    Privilage=models.CharField(max_length=500)

    def get_user_name(self):
        return self.UserName

    def get_user_email(self):
        return self.UserEmail

    def get_user_password(self):
        return self.UserPassword

    def get_user_age(self):
        return self.UserAge

    def get_gender(self):
        return self.Gender

    def get_address(self):
        return self.Address

    def get_postal_code(self):
        return self.PostalCode

    def get_date_registered(self):
        return self.DateRegistered

    def get_notes(self):
        return self.Notes

    def get_tokens(self):
        return self.Tokens

    def get_privilage(self):
        return self.Privilage

    def set_user_name(self, value):
        self.UserName = value

    def set_user_email(self, value):
        self.UserEmail = value

    def set_user_password(self, value):
        self.UserPassword = value

    def set_user_age(self, value):
        self.UserAge = value

    def set_gender(self, value):
        self.Gender = value

    def set_address(self, value):
        self.Address = value

    def set_postal_code(self, value):
        self.PostalCode = value

    def set_date_registered(self, value):
        self.DateRegistered = value

    def set_notes(self, value):
        self.Notes = value

    def set_tokens(self, value):
        self.Tokens = value

    def set_privilage(self, value):
        self.Privilage = value
    
    def get_is_auhtorized(self):
        return self.IsAuhtorized

    def set_is_auhtorized(self, value):
        self.IsAuhtorized = value
