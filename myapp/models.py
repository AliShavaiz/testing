from django.db import models

# Create your models here.


class Student(models.Model):
    name         =  models.CharField(max_length=200)
    fullname         =  models.CharField(max_length=200)
    contact_no       =  models.CharField(max_length=13)
    email         =  models.CharField(max_length=200)
    department          =  models.CharField(max_length=200)
    location  = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name