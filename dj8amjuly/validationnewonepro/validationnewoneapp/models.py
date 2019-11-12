from django.db import models

class RegistrationData(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
