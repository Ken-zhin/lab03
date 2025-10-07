from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    date_registered = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=12, default="")

    def __str__(self):
        return self.username