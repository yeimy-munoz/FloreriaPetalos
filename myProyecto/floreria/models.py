from django.db import models

# Create your models here.
class Flores(models.Model):
    name=models.CharField(max_length=100, primary_key=True)
    fotografia=models.ImageField(upload_to="flor",null=True)
    precio=models.IntegerField()
    descripcion=models.TextField()
    estado=models.TextField()
    stock=models.IntegerField()
    def __str__(self):
        return self.name
