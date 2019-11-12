from django.db import models
from multiselectfield import MultiSelectField


class EnquiryData(models.Model):
    # we use post.get
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=100)
    COURSES_CHOICES = (
        ('PY', 'PYTHON'),
        ('Dj', 'Django'),
        ('RA', 'Rest API'),
        ('Ui', 'UI')
    )
    # course is a variable
    courses = MultiSelectField(choices=COURSES_CHOICES)

    SHIFT_CHOICE = (
        ('Morning', 'Morning Shift'),
        ('Afternoon', 'Afternoon Shift'),
        ('Evening', 'Evening Shift'),
        ('Night', 'Night Shift')
    )
    # shifts is a variable.
    shifts = MultiSelectField(choices=SHIFT_CHOICE)

    start_date = models.DateTimeField(max_length=100)
