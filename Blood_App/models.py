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

    def __unicode__(self):
        return self.group

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
    dob = models.DateField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    contact = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):

        return self.user.username

class BloodPouch(models.Model):
     address = models.ForeignKey(Address)
     chlorestrol_level = models.FloatField()
     donated_by = models.ForeignKey(RegisteredUser)
     quantity = models.IntegerField()
     is_requested = models.IntegerField(default=0)
     blood_type = models.ForeignKey(BloodGroup)

class Request(models.Model):
    requested_by = models.ForeignKey(RegisteredUser)
    requested_pouch = models.ForeignKey(BloodPouch)
    quantity_needed = models.FloatField(null=True)
    is_issued = models.IntegerField(default=0)
    reason = models.CharField(max_length=512,null=True)
