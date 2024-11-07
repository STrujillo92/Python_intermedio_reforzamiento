from django.db import models

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.TextField(default='')
