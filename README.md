# AWS Python HTTP API Project

Este proyecto está estructurado en varias carpetas, cada una con un propósito específico. A continuación, se explica cómo iniciar cada parte del proyecto.

## Estructura del Proyecto

- **`fastapi`**: Contiene la aplicación FastAPI.
- **`serverless`**: Contiene la configuración para desplegar la aplicación usando Serverless Framework.
- **`db1`** y **`db2`**: Contienen configuraciones de bases de datos MySQL con Docker.

## Iniciar el Proyecto

### FastAPI

1. Navega a la carpeta `fastapi`:
   ```bash
   cd fastapi
Instala las dependencias:

bash
Copy
pip install -r requirements.txt
Inicia la aplicación con Uvicorn:

bash
Copy
uvicorn main:app --reload
La aplicación estará disponible en http://127.0.0.1:8000.

Serverless
Navega a la carpeta raíz del proyecto (donde está serverless.yml):

bash
Copy
cd aws-python-http-api-project
Instala las dependencias de Node.js:

bash
Copy
npm install
Inicia Serverless Offline para probar localmente:

bash
Copy
serverless offline --stage dev --reloadHandler
La API estará disponible en http://localhost:3000.

Bases de Datos (MySQL con Docker)
Base de Datos 1 (db1)
Navega a la carpeta db1:

bash
Copy
cd db1
Inicia el contenedor de Docker:

bash
Copy
docker-compose up -d
La base de datos estará disponible en localhost:3306.

Base de Datos 2 (db2)
Navega a la carpeta db2:

bash
Copy
cd db2
Inicia el contenedor de Docker:

bash
Copy
docker-compose up -d
La base de datos estará disponible en localhost:3307.

Configuración Adicional
.gitignore: Archivo para ignorar archivos y carpetas en el control de versiones.

handler.py: Contiene la lógica de las funciones Lambda.

README.md: Este archivo, con instrucciones para el proyecto.
