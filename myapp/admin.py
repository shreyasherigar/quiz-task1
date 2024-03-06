from django.contrib import admin
from .models import questions,register,UserResponse

# Register your models here.
admin.site.register(questions)
admin.site.register(register)
admin.site.register(UserResponse)



