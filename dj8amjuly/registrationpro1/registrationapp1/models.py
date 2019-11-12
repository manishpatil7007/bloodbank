from django.db import models

class ManishData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    UserName=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=100)




