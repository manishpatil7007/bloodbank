from django.conf.urls import url
from django.contrib import admin
from validationapp1.views import RegForm_Page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'$',RegForm_Page)
]
