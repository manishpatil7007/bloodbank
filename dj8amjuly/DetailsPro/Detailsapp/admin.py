from django.contrib import admin
from .models import stud,cours

class Adminstud(admin.ModelAdmin):
    list_display = ['name','location','email']
class Admincours(admin.ModelAdmin):
    list_display = ['cname','cost']
admin.site.register(stud,Adminstud)
admin.site.register(cours,Admincours)


# Register your models here.
