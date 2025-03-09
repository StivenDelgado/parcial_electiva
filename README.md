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
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

3. Inicia la aplicación con Uvicorn:
   ```bash
   uvicorn main:app --reload
La aplicación estará disponible en `http://127.0.0.1:8000`.

### Serverless

1. Navega a la carpeta raíz del proyecto (donde está serverless.yml):
   ```bash
   cd aws-python-http-api-project
   
2. Instala las dependencias de Node.js:
   ```bash
   npm install
   
3. Inicia Serverless Offline para probar localmente:
   ```bash
   serverless offline --stage dev --reloadHandler
   
La API estará disponible en `http://localhost:3000`.

### Bases de Datos (MySQL con Docker)
## Base de Datos 1 (db1)
1. Navega a la carpeta db1:
   ```bash
   cd db1
   
2. Construir las imágenes de Docker:
   ```bash
   docker compose build --no-cache
   
3. Inicia el contenedor de Docker:
   ```bash
   docker compose up -d
   
Mysql estará disponible en `localhost:4600`.
El gestor estará disponible en `localhost:8001`

## Base de Datos 2 (db2)
1. Navega a la carpeta db2:
   ```bash
   cd db2
   
2. Construir las imágenes de Docker:
   ```bash
   docker compose build --no-cache
   
3. Inicia el contenedor de Docker:
   ```bash
   docker compose up -d
   
Mysql estará disponible en `localhost:4800`.
El gestor estará disponible en `localhost:9001`

README.md: Este archivo, con instrucciones para el proyecto.
