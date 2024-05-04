from django.db import models

# Create your models here.

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=100, default='alum')
    def __str__(self):
        return self.rol


class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    assignatures = models.CharField(max_length=200)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.nom} {self.cognom} {self.rol} {self.assignatures}'



