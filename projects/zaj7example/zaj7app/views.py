from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms

# Create your views here.

def generic_address_view(request, post_id, AddressForm):
  instance = None
  if post_id is not None:
    instance = get_object_or_404(models.Address,pk=post_id)
  if request.method == 'POST':
    form = AddressForm(request.POST, instance=instance)
    if form.is_valid():
      form.save()
      return redirect("form-list")
  elif request.method == 'GET':
    form = AddressForm(instance=instance)
  else:
    return HttpResponse(status=405)

  ctx = {'form': form}

  return render(request, "zaj7app/add_form.html", ctx)

def list(request):
  return render(request, "zaj7app/list.html", {
    'adresses': models.Address.objects.all()
  })


def add_address_a(request, post_id=None):
  return generic_address_view(request, post_id, forms.AddressFormA)


def add_address_b(request, post_id=None):
  return generic_address_view(request, post_id, forms.AddressFormB)