from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length = 40)
    stud_class = models.TextField()
    department = models.TextField()


class Market(models.Model):
    usrnm = models.TextField()
    email = models.TextField()
    psw = models.TextField()


class Customer(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    country = models.TextField()
    subject = models.TextField()