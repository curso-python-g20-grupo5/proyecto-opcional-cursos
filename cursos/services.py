from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(nombre, descripcion):
    return Curso.objects.create(nombre=nombre, descripcion=descripcion)

def crear_profesor(nombre, email, direccion=None):
    if direccion:
        direccion = Direccion.objects.create(**direccion)
    return Profesor.objects.create(nombre=nombre, email=email, direccion=direccion)

def crear_estudiante(nombre, email, direccion=None):
    if direccion:
        direccion = Direccion.objects.create(**direccion)
    return Estudiante.objects.create(nombre=nombre, email=email, direccion=direccion)

def crear_direccion(calle, ciudad, pais):
    return Direccion.objects.create(calle=calle, ciudad=ciudad, pais=pais)

def obtiene_estudiante(email):
    return Estudiante.objects.filter(email=email).first()

def obtiene_profesor(email):
    return Profesor.objects.filter(email=email).first()

def obtiene_curso(nombre):
    return Curso.objects.filter(nombre=nombre).first()

def agrega_profesor_a_curso(profesor_email, curso_nombre):
    profesor = obtiene_profesor(profesor_email)
    curso = obtiene_curso(curso_nombre)
    if profesor and curso:
        curso.profesores.add(profesor)
        return True
    return False

def agrega_cursos_a_estudiante(estudiante_email, cursos_nombres):
    estudiante = obtiene_estudiante(estudiante_email)
    if estudiante:
        cursos = Curso.objects.filter(nombre__in=cursos_nombres)
        estudiante.cursos.add(*cursos)
        return True
    return False

def imprime_estudiante_cursos(estudiante_email):
    estudiante = obtiene_estudiante(estudiante_email)
    if estudiante:
        return [curso.nombre for curso in estudiante.cursos.all()]
    return []
