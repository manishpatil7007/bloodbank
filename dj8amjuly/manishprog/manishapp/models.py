from django.db import models

class Emp(models.Model):
    employeeno=models.IntegerField()
    employeename=models.CharField(max_length=100)
    employeesal=models.IntegerField()
    employeeemail=models.EmailField(max_length=100)
    def __str__(self):
        return self.employeename
    


