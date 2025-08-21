from django.db import models

#Clase Prestamo: --
#Clase Lector: -- 
#CLase Biblioteca: Hecho
#Clase Direccion: Hecho
#CLase Comuna: Hecho 
#Clase Libro: --
#Clase Autor: Hecho
#CLase Nacionalidad: Hecho 

# Create your models here.
class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    comuna = models.CharField(max_length=50, null=False)

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=False)
    nacionalidad = models.CharField(max_length=50, null=False)

class Autor(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    pseudonimo = models.CharField(max_length=50, null=False)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField()

class Direccion(models.Model):
    codigo_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=20, null=True)
    departamento = models.CharField(max_length=10, null=True)

"""
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    Genero = models.CharField(max_length=50, null=False)
    titulo = models.CharField(max_length=50, null=False)
"""