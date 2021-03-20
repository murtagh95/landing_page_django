from django.db import models

# Create your models here.
class Registrado(models.Model):
    # Creamos un campo de tipo varchar con un maximo de 100 caracteres,
    # el campo podra ser nullo y no sera required en el formulario
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email
