from django.db import models

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.pais}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, null=True, blank=True)
    cursos = models.ManyToManyField('Curso', related_name='estudiantes')

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    profesores = models.ManyToManyField(Profesor, related_name='cursos')

    def __str__(self):
        return self.nombre

