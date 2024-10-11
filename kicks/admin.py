from django.contrib import admin
from .models import User, Member
# Register your models here.

admin.site.register(Member)
admin.site.register(User)