from django.contrib import admin
from .models import emp,info

class Adminemp(admin.ModelAdmin):
    list_display = ['eno','elocation','eemail','ename']

class Admininfo(admin.ModelAdmin):
    list_display = ['edesignation','esalary']

admin.site.register(emp,Adminemp)
admin.site.register(info,Admininfo)

# Register your models here.
