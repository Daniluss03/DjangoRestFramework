from django.db import models

# Create your models here.
class FormularioContacto(models.Model):
    name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    gmail= models.CharField(max_length=200)
    fecha_pub = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now=True)