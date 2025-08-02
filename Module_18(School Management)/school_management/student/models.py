from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length= 50, verbose_name="Student Name")
    roll= models.IntegerField(unique=True)
    father_name = models.CharField(max_length=50, blank=True,null=True)

#for changing databse items name
    def __str__(self):
        return f"{self.name}, {self.roll}"