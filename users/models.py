from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=255, unique=True)


    def __str__(self):
        return self.email   

    