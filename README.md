# Proyecto Django: Cursos

Este proyecto es una aplicación Django diseñada para administrar cursos, profesores, estudiantes y direcciones. Permite gestionar información relacionada con una institución educativa, mostrando datos en un sitio web y proporcionando funcionalidades básicas para interactuar con la base de datos.

---

## Características

- **Gestión de Cursos**: Agregar, visualizar y asignar cursos.
- **Gestión de Profesores**: Asociar profesores con cursos y mantener información de contacto.
- **Gestión de Estudiantes**: Registrar estudiantes y asignarles múltiples cursos.
- **Gestión de Direcciones**: Asociar direcciones con profesores y estudiantes.
- **Relaciones**: Modelos con relaciones uno a uno, muchos a uno y muchos a muchos.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- Django 4.2 o superior
- PostgreSQL (opcional, puedes usar SQLite para desarrollo)

---

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd opcional_cursos

2. **Crear un entorno virtual**:

   python -m venv venv
   source venv/bin/activate   # En Windows: .\venv\Scripts\activate

3. **Instalar dependencias**:
   pip install -r requirements.txt

4. **Configurar la base de datos**:
   Edita el archivo settings.py y ajusta la configuración de la base de datos en la sección DATABASES.
   El proyecto usa PostgreSQL.

5. **Aplicar migraciones**:
   python manage.py makemigrations
   python manage.py migrate

6. **Crear un superusuario para el panel de administración**:
   python manage.py createsuperuser

6. **Iniciar el servidor de desarrollo**:
   python manage.py runserver
   Accede a la aplicación en: http://127.0.0.1:8000

---

## Estructura del Proyecto
  ![Captura de pantalla 2024-11-25 211920](https://github.com/user-attachments/assets/3a34dba4-6a4a-4137-82f7-142326eb6f73)


---

## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)

⌨️ con ❤️ por el Grupo 3 - G20 😊



