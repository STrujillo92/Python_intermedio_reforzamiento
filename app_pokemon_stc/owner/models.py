from django.db import models

# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    pais = models.CharField(max_length=50, default='')
    habilitado = models.BooleanField(default=False)