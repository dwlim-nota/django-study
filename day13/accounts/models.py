from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    age = models.IntegerField()

    def __str__(self):
        return f"{self.username}"