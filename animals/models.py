from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age = models.IntegerField()
    weight = models.FloatField()
    
    group = models.ForeignKey(
        to="groups.Group", on_delete=models.CASCADE, related_name="animals"
    )
    
    characteristics = models.ManyToManyField(to="characteristics.Characteristic")
