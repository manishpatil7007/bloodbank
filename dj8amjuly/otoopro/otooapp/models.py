from django.db import models

class student1(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    def __str__(self):
        return self.name
class course1(models.Model):
    abc=models.OneToOneField(student1,
                             on_delete=models.CASCADE,null=True)
    cname=models.CharField(max_length=100)
    cost=models.IntegerField()



# Create your models here.
