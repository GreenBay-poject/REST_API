from django.contrib import admin
from app.Models.Questions import Questions
from app.Models.Users import Users
from app.Models.AuthPrivilage import AuthPrivilage
from app.Models.GeneralPrivilage import GeneralPrivilage
from app.Models.Ministry import Ministry

admin.site.register(GeneralPrivilage)
admin.site.register(Questions)
admin.site.register(AuthPrivilage)
admin.site.register(Ministry)
admin.site.register(Users)