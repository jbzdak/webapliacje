from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
  url('^index/?$', views.index),
  url('^edit/?$', views.edit_post)
]
