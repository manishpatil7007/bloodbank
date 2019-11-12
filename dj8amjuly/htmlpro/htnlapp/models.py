from django.db import models

class CustData(models.Model):
    cname=models.CharField(max_length=100)
    num=models.IntegerField()
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)

