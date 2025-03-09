# PARCIAL
This project is structured into several folders, each with a specific purpose. Below is an explanation of how to start each part of the project.

## Project Structure
- **`fastapi`**: Contains the FastAPI application.

- **`serverless`**: Contains the configuration to deploy the application using the Serverless Framework.

- **`db1`** y **`db2`**: Contain MySQL database configurations with Docker.

## Starting the Project
### FastAPI
1. Navigate to the `fastapi` folder:
   ```bash
   cd fastapi
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
3. Start the application with Uvicorn:
   ```bash
   uvicorn main:app --reload
The application will be available at `http://127.0.0.1:8000`.

### Serverless
1. Navigate to the project root folder (where serverless.yml is located):
   ```bash
   cd aws-python-http-api-project
2. Install Node.js dependencies:
   ```bash
   npm install
3. Start Serverless Offline to test locally:
   ```bash
   serverless offline --stage dev --reloadHandler
The API will be available at `http://localhost:3000`.

## Databases (MySQL with Docker)
### Database 1 (db1)
1. Navigate to the db1 folder:
   ```bash
   cd db1
   
2. Build the Docker images:
   ```bash
   docker compose build --no-cache

3. Start the Docker container:
   ```bash
   docker compose up -d
   
MySQL will be available at `localhost:4600`.
The management interface will be available at `localhost:8001`.

### Database 2 (db2)
1. Navigate to the db2 folder:
   ```bash
   cd db2
   
2. Build the Docker images:
   ```bash
   docker compose build --no-cache

3. Start the Docker container:
   ```bash
   docker compose up -d
   
MySQL will be available at `localhost:4800`.
The management interface will be available at `localhost:9001`.

README.md: This file, with instructions for the project.
