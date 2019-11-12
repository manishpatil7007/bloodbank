from django.contrib import admin
from .models import student1,course1


class Adminstudent1(admin.ModelAdmin):
     list_display = ['name','location','email']
class Admincourse1(admin.ModelAdmin):
     list_display = ['cname','cost']
admin.site.register(student1,Adminstudent1)
admin.site.register(course1,Admincourse1)
