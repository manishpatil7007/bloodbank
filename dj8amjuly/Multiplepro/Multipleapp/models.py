from django.db import models

class Customer(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    salesamt=models.IntegerField()
class Emp(models.Model):
    eid = models.AutoField(primary_key=True)
    ename=models.CharField(max_length=100)
    salary=models.IntegerField()
class Skills(models.Model):
    Skid = models.AutoField(primary_key=True)
    skname=models.CharField(max_length=100)
    cost=models.IntegerField()
class Student(Customer,Emp,Skills):
    Sid = models.AutoField(primary_key=True)
    sname=models.CharField(max_length=100)
    marks=models.IntegerField()


# Create your models here.
