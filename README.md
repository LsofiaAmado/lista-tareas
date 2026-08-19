# API Lista de Tareas

API REST desarrollada con **Django** y **Django REST Framework** para gestionar una lista de tareas mediante operaciones CRUD (Crear, Consultar, Actualizar y Eliminar).

La aplicación utiliza **MariaDB** como sistema de gestión de base de datos y cuenta con autenticación básica para proteger los endpoints.

---

## Tecnologías utilizadas

* Python 3
* Django 6.1
* Django REST Framework
* MariaDB 12.3
* mysqlclient
* DBeaver
* Postman
* Git

---

## Funcionalidades

La API permite:

* Crear tareas.
* Consultar todas las tareas.
* Consultar una tarea por su identificador.
* Actualizar una tarea.
* Eliminar una tarea.
* Proteger los endpoints mediante autenticación básica.
* Almacenar la información utilizando MariaDB.

---

## Estructura del proyecto

```text
API-LISTA-TAREAS/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tareas/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── database.sql
├── .gitignore
└── README.md
```

> La carpeta `venv/` se utiliza únicamente para el entorno virtual local y no debe subirse al repositorio.

---

# Requisitos previos

Antes de ejecutar el proyecto se debe tener instalado:

* Python 3
* MariaDB
* Git
* DBeaver (opcional, para administrar visualmente la base de datos)
* Postman (opcional, para realizar pruebas de la API)

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar en la carpeta:

```bash
cd API-LISTA-TAREAS
```

---

## 2. Crear el entorno virtual

En Windows:

```bash
python -m venv venv
```

Activar el entorno virtual utilizando Git Bash:

```bash
source venv/Scripts/activate
```

En PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo aparecerá:

```text
(venv)
```

---

## 3. Instalar las dependencias

Con el entorno virtual activo:

```bash
pip install -r requirements.txt
```

Las principales dependencias utilizadas son:

* Django
* Django REST Framework
* mysqlclient

---

# Configuración de MariaDB

## 1. Crear la base de datos

En MariaDB se debe crear la base de datos:

```sql
CREATE DATABASE lista_tareas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

También se puede utilizar el archivo:

```text
database.sql
```

incluido en el proyecto.

---

## 2. Configurar la conexión

En:

```text
config/settings.py
```

se configura la conexión con MariaDB.

Ejemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lista_tareas',
        'USER': 'root',
        'PASSWORD': 'TU_CONTRASEÑA',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> Por seguridad, la contraseña real no debe almacenarse directamente en un repositorio público. Se recomienda utilizar variables de entorno.

---

# Migraciones

Después de configurar la base de datos se deben ejecutar:

```bash
python manage.py makemigrations
```

y:

```bash
python manage.py migrate
```

Esto crea las tablas necesarias en MariaDB.

La tabla principal de la aplicación es:

```text
tareas_tarea
```

con los siguientes campos:

| Campo       | Descripción                     |
| ----------- | ------------------------------- |
| id          | Identificador único de la tarea |
| titulo      | Título de la tarea              |
| descripcion | Descripción de la tarea         |

---

# Crear usuario para autenticación

La API utiliza **Basic Authentication**.

Para crear un usuario:

```bash
python manage.py createsuperuser
```

Django solicitará:

```text
Username:
Email address:
Password:
Password (again):
```

Las credenciales creadas serán utilizadas para autenticarse en las peticiones a la API.

---

# Ejecutar la aplicación

Con el entorno virtual activo:

```bash
python manage.py runserver
```

La API estará disponible en:

```text
http://127.0.0.1:8000/
```

---

# Endpoints

## Listar tareas

```http
GET /api/tareas/
```

Ejemplo:

```text
http://127.0.0.1:8000/api/tareas/
```

Respuesta:

```json
[
    {
        "id": 1,
        "titulo": "Aprender Django",
        "descripcion": "Crear una API REST"
    }
]
```

---

## Crear una tarea

```http
POST /api/tareas/
```

URL:

```text
http://127.0.0.1:8000/api/tareas/
```

Body:

```json
{
    "titulo": "Nueva tarea",
    "descripcion": "Descripción de la nueva tarea"
}
```

Respuesta esperada:

```json
{
    "id": 2,
    "titulo": "Nueva tarea",
    "descripcion": "Descripción de la nueva tarea"
}
```

Código de respuesta:

```text
201 Created
```

---

## Consultar una tarea

```http
GET /api/tareas/{id}/
```

Ejemplo:

```text
http://127.0.0.1:8000/api/tareas/1/
```

Respuesta:

```json
{
    "id": 1,
    "titulo": "Aprender Django",
    "descripcion": "Crear una API REST"
}
```

---

## Actualizar una tarea

```http
PUT /api/tareas/{id}/
```

Ejemplo:

```text
http://127.0.0.1:8000/api/tareas/1/
```

Body:

```json
{
    "titulo": "Tarea actualizada",
    "descripcion": "Descripción actualizada"
}
```

Respuesta esperada:

```json
{
    "id": 1,
    "titulo": "Tarea actualizada",
    "descripcion": "Descripción actualizada"
}
```

Código de respuesta:

```text
200 OK
```

> Las URLs de tareas específicas incluyen `/` al final.

---

## Eliminar una tarea

```http
DELETE /api/tareas/{id}/
```

Ejemplo:

```text
http://127.0.0.1:8000/api/tareas/1/
```

Respuesta:

```text
204 No Content
```

---

# Autenticación

Los endpoints de la API están protegidos mediante **HTTP Basic Authentication**.

En Postman:

1. Seleccionar la petición.
2. Ir a **Authorization**.
3. En **Type**, seleccionar **Basic Auth**.
4. Introducir el usuario creado mediante `createsuperuser`.
5. Introducir la contraseña correspondiente.
6. Presionar **Send**.

Ejemplo:

```text
Authorization
Type: Basic Auth

Username: admin_api
Password: ********
```

Las peticiones sin autenticación reciben:

```text
401 Unauthorized
```

Esto permite restringir el acceso a las operaciones de la API.

---

# Pruebas con Postman

Las operaciones CRUD fueron probadas utilizando Postman.

| Método | Endpoint            | Función          |
| ------ | ------------------- | ---------------- |
| GET    | `/api/tareas/`      | Listar tareas    |
| POST   | `/api/tareas/`      | Crear tarea      |
| GET    | `/api/tareas/{id}/` | Consultar tarea  |
| PUT    | `/api/tareas/{id}/` | Actualizar tarea |
| DELETE | `/api/tareas/{id}/` | Eliminar tarea   |

Las peticiones deben incluir autenticación mediante **Basic Auth**.

---

# Base de datos

La aplicación utiliza MariaDB con la siguiente estructura:

```text
lista_tareas
│
└── tareas_tarea
    ├── id
    ├── titulo
    └── descripcion
```

El modelo Django correspondiente es:

```python
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
```

---

# Flujo de la aplicación

```text
Cliente / Front-end
        │
        │ HTTP + JSON
        ▼
Django REST Framework
        │
        │ Basic Authentication
        ▼
     Serializer
        │
        ▼
    Django ORM
        │
        ▼
      MariaDB
        │
        ▼
   tareas_tarea
```

---

# Códigos de respuesta principales

| Código | Significado                     |
| ------ | ------------------------------- |
| 200    | Operación exitosa               |
| 201    | Recurso creado                  |
| 204    | Recurso eliminado correctamente |
| 400    | Solicitud incorrecta            |
| 401    | No autenticado                  |
| 404    | Recurso no encontrado           |
| 500    | Error interno del servidor      |

---

# Ejecución rápida

Después de clonar el proyecto:

```bash
python -m venv venv
```

Activar:

```bash
source venv/Scripts/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Configurar MariaDB y crear:

```text
lista_tareas
```

Ejecutar migraciones:

```bash
python manage.py migrate
```

Crear usuario:

```bash
python manage.py createsuperuser
```

Ejecutar servidor:

```bash
python manage.py runserver
```

API:

```text
http://127.0.0.1:8000/api/tareas/
```

---


Proyecto desarrollado como prueba técnica para la implementación de una API REST de gestión de tareas utilizando Django, Django REST Framework y MariaDB.
