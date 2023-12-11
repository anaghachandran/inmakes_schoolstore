from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    materials_provide = models.ManyToManyField('Materials')
class Materials(models.Model):
    name = models.CharField(max_length=255)

