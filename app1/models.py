from django.utils import timezone
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null= False, blank=False)
    cedula = models.CharField(max_length=10, null=False, blank=False, primary_key=True)

    def __str__(self):
        return self.nombre

class Lista(models.Model):
    nombre_lista = models.CharField(max_length=50, null= False, default="")

    def __str__(self):
        return self.nombre_lista

class Candidato(models.Model):     
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='images/', verbose_name='Image', null=True)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre
    
class Voto(models.Model):
    nombre_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    cedula_votante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.nombre_candidato}  | {self.cedula_votante}"