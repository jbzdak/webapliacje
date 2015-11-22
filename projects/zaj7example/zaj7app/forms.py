
# -*- coding: utf-8 -*-

from django import forms
from localflavor.pl.forms import PLPESELField, PLPostalCodeField, \
  PLProvinceSelect

from . import models

class AddressFormA(forms.ModelForm):

  class Meta:
    model = models.Address
    exclude = ['id']


class AddressFormB(forms.ModelForm):

  zip_code    = PLPostalCodeField(max_length=100)
  voivoidship = forms.CharField(max_length=100, widget=PLProvinceSelect())

  class Meta:
    model = models.Address
    exclude = ['id']
