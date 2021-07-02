from django.db import models

# Create your models here.

class Users(models.Model):
    
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    UserRole = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)

class Appointments(models.Model):
    
    PatientName = models.CharField(max_length=500)
    DoctorName = models.CharField(max_length=500)
    DateOfAppointment = models.DateField()
    TimeOfAppointment = models.TimeField()
class meta:
    app_label= 'HospitalApp'