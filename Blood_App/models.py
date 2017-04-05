from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import re

class BloodGroup(models.Model):
    BLOOD_TYPES = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+','O+'),
    )
    group = models.CharField(max_length=5,choices=BLOOD_TYPES)

class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.CharField(max_length=6)

class RegisteredUser(models.Model):
    GENDER_CHOICES = (
        ('Male', 'M'),
        ('Female', 'F')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    blood_group = models.ForeignKey(BloodGroup)
    dob = models.DateField
    age = models.CharField(max_length=2)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    contact = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

class BloodPouch(models.Model):
     address = models.ForeignKey(Address)
     chlorestrol_level = models.IntegerField
     donated_by = models.ForeignKey(RegisteredUser)
     blood_type = models.CharField(max_length=50)

class Request(models.Model):
    requested_by = models.ForeignKey(RegisteredUser)
    quantity_needed = models.FloatField
    reason = models.CharField(max_length=512)
