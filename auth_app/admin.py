from django.contrib import admin
from auth_app.sub_models.Questions import Questions
from auth_app.sub_models.Users import Users
from auth_app.sub_models.AuthPrivilage import AuthPrivilage
from auth_app.sub_models.GeneralPrivilage import GeneralPrivilage
from auth_app.sub_models.Ministry import Ministry

admin.site.register(GeneralPrivilage)
admin.site.register(Questions)
admin.site.register(AuthPrivilage)
admin.site.register(Ministry)
admin.site.register(Users)