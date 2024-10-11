from django.db import models
from django.utils import timezone
# from django.utils import timezone //shows the time it was created when you have a time slot on the models in line 8

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    # created_at = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return (f"The username is {self.username}  email is {self.email}")
    






class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"