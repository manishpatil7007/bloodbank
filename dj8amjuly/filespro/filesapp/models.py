from django.db import models

class student123(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)
    imag=models.ImageField(upload_to='image')
    def __str__(self):
        return self.sname
