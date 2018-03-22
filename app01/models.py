from django.db import models

# Create your models here.

class Classes(models.Model):
    title = models.CharField(max_length=32)
    m = models.ManyToManyField('Teachers',related_name='sssss')

class Teachers(models.Model):
    name = models.CharField(max_length=32)

class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.NullBooleanField()
    cs = models.ForeignKey(Classes,related_name='ssss')
