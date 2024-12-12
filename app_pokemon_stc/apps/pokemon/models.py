from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    numero = models.IntegerField(default=0)
    generacion = models.CharField(max_length=20)