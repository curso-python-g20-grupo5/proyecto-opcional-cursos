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
Crear un entorno virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate   # En Windows: .\venv\Scripts\activate
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
Configurar la base de datos:

Edita el archivo settings.py y ajusta la configuración de la base de datos en la sección DATABASES.
Por defecto, el proyecto usa SQLite.
Aplicar migraciones:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Crear un superusuario para el panel de administración:

bash
Copiar código
python manage.py createsuperuser
Iniciar el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Accede a la aplicación en: http://127.0.0.1:8000.

Uso
Panel de Administración
El panel de administración está disponible en:

arduino
Copiar código
http://127.0.0.1:8000/admin/
Inicia sesión con las credenciales de superusuario y gestiona los datos de cursos, estudiantes, profesores y direcciones.

Cargar Datos de Prueba
Puedes cargar datos predefinidos usando el comando:

bash
Copiar código
python manage.py loaddata cursos_fixture.json
Visualización de Cursos
La lista de cursos está disponible en:

arduino
Copiar código
http://127.0.0.1:8000/cursos/
Estructura del Proyecto
bash
Copiar código
opcional_cursos/
├── cursos/                     # Aplicación principal
│   ├── migrations/             # Migraciones para la base de datos
│   ├── models.py               # Modelos del proyecto
│   ├── views.py                # Vistas de la aplicación
│   ├── services.py             # Funciones de lógica de negocio
│   ├── urls.py                 # Rutas específicas de la app
│   ├── admin.py                # Configuración del panel de administración
│   ├── serializers.py          # Serializadores para API (opcional)
│   └── templates/cursos/       # Plantillas HTML
├── opcional_cursos/            # Configuración principal del proyecto
│   ├── settings.py             # Configuración global
│   ├── urls.py                 # Rutas del proyecto
│   └── wsgi.py                 # Configuración WSGI
├── db.sqlite3                  # Base de datos SQLite (opcional)
├── manage.py                   # Herramienta de línea de comandos de Django
└── README.md                   # Documentación del proyecto
Dependencias
Django
psycopg2-binary (si usas PostgreSQL)
Django REST Framework (opcional, para APIs)
Contribuir
Si deseas contribuir al proyecto:

Haz un fork del repositorio.
Crea una rama para tu funcionalidad: git checkout -b feature/nueva-funcionalidad.
Realiza tus cambios y súbelos: git commit -m "Agrega nueva funcionalidad".
Envía un pull request.
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto
Desarrollado por: [Tu Nombre]
Email: [tuemail@example.com]

yaml
Copiar código

---

### Personalización
Puedes ajustar las secciones del `README.md` para incluir detalles específicos del proyecto, como rutas adicionales o instrucciones personalizadas. Si necesitas ayuda con algo más, ¡házmelo saber! 😊





