from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class Employee(AbstractUser):
    age = models.IntegerField(default=0)

