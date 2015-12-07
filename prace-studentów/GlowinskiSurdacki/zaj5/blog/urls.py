from django.conf.urls import include, url
from django.contrib import admin
from blog_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url('^index/?$', views.index),
    url('^edit/?$', views.edit),
    url('^post/?$', views.post),
    url('^/?$', views.index),
]
