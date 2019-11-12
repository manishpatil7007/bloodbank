from django.db import models
from multiselectfield import MultiSelectField

class ServicesData1(models.Model):
     course_id=models.IntegerField(primary_key=True)
     course_name=models.CharField(max_length=100,unique=True)
     course_duration=models.CharField(max_length=100)
     course_start_date=models.DateField(max_length=100)
     course_start_time=models.TimeField(max_length=100)
     course_trainer_name=models.CharField(max_length=100)
     course_trainer_exp=models.CharField(max_length=100)

class EnquiryData(models.Model):
     name=models.CharField(max_length=100)
     mobile=models.BigIntegerField()
     email=models.EmailField(max_length=100)
     gender=models.CharField(max_length=100)

     COURSES_CHOICES = (
          ('PY', 'PYTHON'),
          ('Dj', 'Django'),
          ('RA', 'Rest API'),
          ('Ui', 'UI')
     )
     # course is a variable
     course = MultiSelectField(choices=COURSES_CHOICES)

     SHIFT_CHOICE = (
          ('Morning', 'Morning Shift'),
          ('Afternoon', 'Afternoon Shift'),
          ('Evening', 'Evening Shift'),
          ('Night', 'Night Shift')
     )
     # shifts is a variable.
     shifts = MultiSelectField(choices=SHIFT_CHOICE)

     start_date = models.DateTimeField(max_length=100)



