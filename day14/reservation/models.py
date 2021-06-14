from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, related_name="patients")

    def __str__(self):
        return f"{self.name}"
