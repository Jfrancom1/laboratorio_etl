# 🚀 Laboratorio Final — Pipeline ETL con FastAPI  
**Bases de Datos para Ciencia de Datos – Universidad de Antioquia**

## 👥 Integrantes
- Juan Felipe Franco  
- Sebastian Cardona

---

## 📌 Descripción General

Este proyecto implementa una aplicación de **Ingeniería de Datos** que orquesta un pipeline **ETL completo** utilizando:

- FastAPI como backend
- MongoDB como staging (datos crudos)
- Pandas para transformación
- MySQL como Data Warehouse (datos limpios y estructurados)

La fuente de datos es la **Rick & Morty API**, de donde se extraen personajes, se limpian y se almacenan en una tabla SQL plana.

---

## 🧠 Arquitectura

### 🔄 Flujo de Datos (ETL)

Rick & Morty API → MongoDB (Staging) → Pandas (Transformación) → MySQL (Warehouse)

### 🏗️ Patrón Arquitectónico

Se utiliza una arquitectura **MVC + Services**:

- Controllers: Manejan rutas HTTP
- Services: Contienen la lógica del ETL
- Models: Definen las tablas SQL
- Views: Validan requests/responses (Pydantic)

---

## 📁 Estructura del Proyecto

laboratorio_etl/
│── .env
│── .gitignore
│── requirements.txt
│── README.md
│
└── app/
│── main.py
│── config.py
│── database.py
│
├── controllers/
│ └── etl_controller.py
│
├── services/
│ └── etl_service.py
│
├── models/
│ └── personajes_sql.py
│
└── views/
└── schemas.py


---

## ⚙️ Tecnologías Utilizadas

| Tecnología | Uso |
|-----------|-----|
| FastAPI | Backend y API REST |
| MongoDB | Staging de datos crudos |
| Pandas | Transformación de datos |
| MySQL | Data Warehouse |
| SQLAlchemy | ORM para SQL |
| Requests | Consumo de API externa |
| Python-dotenv | Gestión de variables de entorno |

---

## 🔐 Variables de Entorno (`.env`)

MONGO_URI=mongodb://localhost:27017
MONGO_DB=rick_and_morty_staging

MYSQL_USER=root
MYSQL_PASSWORD=tu_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=rick_and_morty_dw

📦 Instalación y Ejecución
1️⃣ Clonar repositorio
git clone https://github.com/Jfrancom1/laboratorio_etl.git
cd laboratorio_etl

2️⃣ Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\activate   # Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Crear base de datos en MySQL
CREATE DATABASE rick_and_morty_dw;

5️⃣ Ejecutar servidor
uvicorn app.main:app --reload

6️⃣ Abrir documentación Swagger
http://127.0.0.1:8000/docs

🌐 Endpoints Disponibles
🔹 1. Extracción (Staging)

POST /api/v1/etl/extraer

Body:

{
  "cantidad": 50
}


Función:

Descarga datos desde la Rick & Morty API

Guarda los JSON crudos en MongoDB

Implementa idempotencia (no duplica registros)

Respuesta:

{
  "mensaje": "Datos extraídos exitosamente",
  "registros_guardados": 50,
  "fuente": "Rick & Morty API",
  "status": 201
}

🔹 2. Transformación y Carga (ETL)

POST /api/v1/etl/transformar

Función:

Lee documentos desde MongoDB

Aplana JSONs con Pandas

Limpia nulos y columnas irrelevantes

Inserta datos en MySQL en una tabla plana

Implementa idempotencia SQL

Respuesta:

{
  "mensaje": "Pipeline finalizado",
  "registros_procesados": 50,
  "tabla_destino": "personajes_master",
  "status": 200
}

🔹 3. Limpieza Total (Reset)

DELETE /api/v1/etl/reset

Función:

Elimina todos los documentos de MongoDB

Borra la tabla SQL en MySQL

Respuesta:

{
  "mensaje": "Sistema reseteado correctamente",
  "mongo_docs_eliminados": 150,
  "mysql_rows_eliminadas": 150,
  "status": 200
}

🗄️ Bases de Datos
📦 MongoDB (Staging)

Base: rick_and_morty_staging

Colección: raw_characters

Contiene los JSON crudos extraídos de la API.

🏛️ MySQL (Data Warehouse)

Base: rick_and_morty_dw

Tabla: personajes_master

Columna	Tipo
id_personaje	INTEGER (PK)
nombre	VARCHAR
estado	VARCHAR
especie	VARCHAR
genero	VARCHAR
origen	VARCHAR
ubicacion	VARCHAR
imagen	VARCHAR
🔁 Idempotencia

Extract: Verifica si el personaje ya existe en MongoDB antes de insertarlo.

Transform/Load: Reemplaza la tabla SQL antes de cargar nuevos datos, evitando duplicados.

🧪 Orden Correcto de Ejecución

DELETE /api/v1/etl/reset

POST /api/v1/etl/extraer

POST /api/v1/etl/transformar

📸 Evidencias Requeridas (PDF de entrega)

✔️ Swagger/Postman: ejecución exitosa de los 3 endpoints

✔️ MongoDB: documentos cargados en raw_characters

✔️ MySQL/DBeaver: tabla personajes_master llena

🎯 Consideraciones de Diseño

Arquitectura modular basada en MVC + Services

Separación clara entre ingesta, transformación y persistencia

Uso de variables de entorno para seguridad

Pipeline reproducible y reiniciable

🧠 Fuente de Datos

API pública:
https://rickandmortyapi.com