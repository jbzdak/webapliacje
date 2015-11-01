from django.conf.urls import include, url
from django.contrib import admin


from zaj3app import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'zaj3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^hello/?$', views.hello_world),
    url('^ask/?$', views.get_name),
    url('^greet/?$', views.greet_by_name),
    # url(r'^admin/', include(admin.site.urls)),
]
