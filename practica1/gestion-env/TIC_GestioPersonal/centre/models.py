from django.db import models

# Create your models here.

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)


class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    assignatures = models.CharField(max_length=200)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)



