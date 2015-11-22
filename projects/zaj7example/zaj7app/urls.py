from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^list/', views.list, name="form-list"),
    url(r'^add/A', views.add_address_a),
    url(r'^edit/A/(?P<post_id>\d+)/?', views.add_address_a),
    url(r'^add/B', views.add_address_b),
    url(r'^edit/B/(?P<post_id>\d+)/?', views.add_address_b),
]
