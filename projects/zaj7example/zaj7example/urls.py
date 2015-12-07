from django.conf.urls import include, url
from django.contrib import admin

from zaj7app import urls as zaj7urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'zaj7example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^address/', include(zaj7urls))
]
