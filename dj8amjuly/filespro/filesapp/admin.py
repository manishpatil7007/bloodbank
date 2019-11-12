from django.contrib import admin
from .models import student123


class student123admin(admin.ModelAdmin):
    list_display = ('sno','snaem','sloc','imag')
admin.site.register(student123,student123admin)

