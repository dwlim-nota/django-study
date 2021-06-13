from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)

class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, related_name="patients")

# class Reservation(models.Model):
#     docter = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reservations')
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reservations')

