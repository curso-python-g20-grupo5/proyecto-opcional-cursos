from django.contrib import admin
from .models import Direccion, Profesor, Estudiante, Curso

admin.site.register(Direccion)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Curso)
