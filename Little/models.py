from django.db import models

class Usuarios(models.Model):
    Apodo = models.CharField(max_length=12)
    Email = models.CharField(max_length=150)
    Contrasena = models.CharField(max_length=255)
    class Meta:
        db_table = 'usuarios'