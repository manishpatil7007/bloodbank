from django.conf.urls import url,include
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'hyd/',views.hyd),
    url(r'bang/',views.bang)
]
