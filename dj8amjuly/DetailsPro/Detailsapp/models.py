from django.db import models
class stud(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    def __str__(self):
        return self.name
class cours(models.Model):
    abcd=models.OneToOneField(stud)
    cname=models.CharField(max_length=100)
    cost=models.CharField(max_length=100)


# Create your models here.
