from django.contrib import admin
from auth_app.sub_models.Posts import Posts
from auth_app.sub_models.Answeres import Answeres
from auth_app.sub_models.Questions import Questions
from auth_app.sub_models.Users import Users
from auth_app.sub_models.AuthPrivilage import AuthPrivilage

admin.site.register(Posts)
admin.site.register(Answeres)
admin.site.register(Questions)
admin.site.register(AuthPrivilage)
admin.site.register(Users)