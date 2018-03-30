from django.db import models

# Create your models here.


class USERS(models.Model):
    user = models.CharField(max_length=32)
    email = models.CharField(max_length=32)