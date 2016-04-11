from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=200)
    studentid = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    github = models.CharField(max_length=20)
    web = models.CharField(max_length=20)
    