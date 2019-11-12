from django.contrib import admin

from .models import ServicesData1

class AdminServicesData1(admin.ModelAdmin):
    list_display = ['course_id',
                    'course_name',
                    'course_duration',
                    'course_start_date',
                    'course_start_time',
                    'course_trainer_name',
                    'course_trainer_exp']
admin.site.register(ServicesData1,AdminServicesData1)

