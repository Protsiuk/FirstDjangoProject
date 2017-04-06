from django.db import models

# Create your models here.
class Member (models.Model):
    username = models.CharField(max_length= 255)
    password = models.CharField(max_length= 255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    def upper_username(self):
        return self.username.upper()