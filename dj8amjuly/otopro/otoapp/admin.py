from django.contrib import admin

from .models import student,course

class Adminstudent(admin.ModelAdmin):
    list_display = ['name','email','location']

class Admincourse(admin.ModelAdmin):
    list_display = ['cname','cost']

admin.site.register(student,Adminstudent)
admin.site.register(course,Admincourse)

# Register your models here.
