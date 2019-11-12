from django.db import models


class Empdata1(models.Model):
    ename=models.CharField(max_length=100)
    salary=models.IntegerField()
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    location=models.CharField(max_length=100)



