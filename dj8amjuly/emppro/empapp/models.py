from django.db import models

class emp(models.Model):
    eno=models.IntegerField()
    eemail = models.EmailField(max_length=100)
    ename=models.CharField(max_length=100)
    elocation=models.CharField(max_length=100)


    def __str__(self):
        return self.ename
class info(models.Model):
    abc=models.OneToOneField(emp,on_delete=emp)
    edesignation=models.CharField(max_length=100)
    esalary=models.IntegerField()


# Create your models here.
