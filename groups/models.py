from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    name = models.FloatField()
    sex = models.CharField(max_length=15)