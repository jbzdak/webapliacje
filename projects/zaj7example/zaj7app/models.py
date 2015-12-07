from django.db import models

from localflavor.pl.forms import  PLPESELField

# Create your models here.

class Address(models.Model):

  street_address = models.CharField(verbose_name="Street address", max_length=100)
  street_no = models.CharField(verbose_name="Street number", max_length=100)
  zip_code = models.CharField(verbose_name="zip-code", max_length=10)
  city = models.CharField(verbose_name="City", max_length=100)
  voivoidship = models.CharField(verbose_name="Voivoidshio", max_length=100)

class Student(models.Model):

  name = models.CharField(max_length=100)
  pesel = models.CharField(max_length=100)

  # Address
