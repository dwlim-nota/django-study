from django.db import models

# Create your models here.

##############################################################################
# 2. user model 확장

class MyUser(AbstractUser):
    age = models.IntegerField(default=0)

