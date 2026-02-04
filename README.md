<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Laboratorio ETL - Rick & Morty</title>
</head>
<body>

  <h1>🚀 Laboratorio Final — Pipeline ETL con FastAPI</h1>
  <h2>Bases de Datos para Ciencia de Datos – Universidad de Antioquia</h2>

  <div class="box">
    <h3>👥 Integrantes</h3>
    <ul>
      <li>Juan Felipe Franco</li>
      <li>Sebastian Cardona</li>
    </ul>
  </div>

  <div class="box">
    <h3>📌 Descripción General</h3>
    <p>
      Este proyecto implementa una aplicación de <strong>Ingeniería de Datos</strong> que orquesta
      un pipeline <strong>ETL completo</strong> utilizando:
    </p>
    <ul>
      <li>FastAPI como backend</li>
      <li>MongoDB como staging (datos crudos)</li>
      <li>Pandas para transformación</li>
      <li>MySQL como Data Warehouse (datos limpios y estructurados)</li>
    </ul>
    <p>
      La fuente de datos es la <strong>Rick & Morty API</strong>, de donde se extraen personajes,
      se limpian y se almacenan en una tabla SQL plana.
    </p>
  </div>

  <div class="box">
    <h3>🧠 Arquitectura</h3>
    <h4>🔄 Flujo de Datos (ETL)</h4>
    <pre>
Rick & Morty API → MongoDB (Staging) → Pandas (Transformación) → MySQL (Warehouse)
    </pre>

    <h4>🏗️ Patrón Arquitectónico</h4>
    <p>Se utiliza una arquitectura <strong>MVC + Services</strong>:</p>
    <ul>
      <li><strong>Controllers:</strong> Manejan rutas HTTP</li>
      <li><strong>Services:</strong> Contienen la lógica del ETL</li>
      <li><strong>Models:</strong> Definen las tablas SQL</li>
      <li><strong>Views:</strong> Validan requests/responses (Pydantic)</li>
    </ul>
  </div>

  <div class="box">
    <h3>📁 Estructura del Proyecto</h3>
    <pre>
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
    │   └── etl_controller.py
    │
    ├── services/
    │   └── etl_service.py
    │
    ├── models/
    │   └── personajes_sql.py
    │
    └── views/
        └── schemas.py
    </pre>
  </div>

  <div class="box">
    <h3>⚙️ Tecnologías Utilizadas</h3>
    <table>
      <tr>
        <th>Tecnología</th>
        <th>Uso</th>
      </tr>
      <tr>
        <td>FastAPI</td>
        <td>Backend y API REST</td>
      </tr>
      <tr>
        <td>MongoDB</td>
        <td>Staging de datos crudos</td>
      </tr>
      <tr>
        <td>Pandas</td>
        <td>Transformación de datos</td>
      </tr>
      <tr>
        <td>MySQL</td>
        <td>Data Warehouse</td>
      </tr>
      <tr>
        <td>SQLAlchemy</td>
        <td>ORM para SQL</td>
      </tr>
      <tr>
        <td>Requests</td>
        <td>Consumo de API externa</td>
      </tr>
      <tr>
        <td>Python-dotenv</td>
        <td>Gestión de variables de entorno</td>
      </tr>
    </table>
  </div>

  <div class="box">
    <h3>🔐 Variables de Entorno (<code>.env</code>)</h3>
    <pre>
MONGO_URI=mongodb://localhost:27017
MONGO_DB=rick_and_morty_staging

MYSQL_USER=root
MYSQL_PASSWORD=tu_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=rick_and_morty_dw
    </pre>
    <p><strong>Nota:</strong> Este archivo no se sube al repositorio por seguridad.</p>
  </div>

  <div class="box">
    <h3>📦 Instalación y Ejecución</h3>

    <h4>1️⃣ Clonar repositorio</h4>
    <pre>
git clone https://github.com/Jfrancom1/laboratorio_etl.git
cd laboratorio_etl
    </pre>

    <h4>2️⃣ Crear y activar entorno virtual</h4>
    <pre>
python -m venv .venv
.venv\Scripts\activate   # Windows
    </pre>

    <h4>3️⃣ Instalar dependencias</h4>
    <pre>
pip install -r requirements.txt
    </pre>

    <h4>4️⃣ Crear base de datos en MySQL</h4>
    <pre>
CREATE DATABASE rick_and_morty_dw;
    </pre>

    <h4>5️⃣ Ejecutar servidor</h4>
    <pre>
uvicorn app.main:app --reload
    </pre>

    <h4>6️⃣ Abrir documentación Swagger</h4>
    <pre>
http://127.0.0.1:8000/docs
    </pre>
  </div>

  <div class="box">
    <h3>🌐 Endpoints Disponibles</h3>

    <h4>🔹 1. Extracción (Staging)</h4>
    <p><strong>POST</strong> <code>/api/v1/etl/extraer</code></p>
    <p>Body:</p>
    <pre>
{
  "cantidad": 50
}
    </pre>
    <p>
      Función:
      <ul>
        <li>Descarga datos desde la Rick & Morty API</li>
        <li>Guarda los JSON crudos en MongoDB</li>
        <li>Implementa idempotencia (no duplica registros)</li>
      </ul>
    </p>
    <p>Respuesta:</p>
    <pre>
{
  "mensaje": "Datos extraídos exitosamente",
  "registros_guardados": 50,
  "fuente": "Rick & Morty API",
  "status": 201
}
    </pre>

    <h4>🔹 2. Transformación y Carga (ETL)</h4>
    <p><strong>POST</strong> <code>/api/v1/etl/transformar</code></p>
    <p>
      Función:
      <ul>
        <li>Lee documentos desde MongoDB</li>
        <li>Aplana JSONs con Pandas</li>
        <li>Limpia nulos y columnas irrelevantes</li>
        <li>Inserta datos en MySQL en una tabla plana</li>
        <li>Implementa idempotencia SQL</li>
      </ul>
    </p>
    <p>Respuesta:</p>
    <pre>
{
  "mensaje": "Pipeline finalizado",
  "registros_procesados": 50,
  "tabla_destino": "personajes_master",
  "status": 200
}
    </pre>

    <h4>🔹 3. Limpieza Total (Reset)</h4>
    <p><strong>DELETE</strong> <code>/api/v1/etl/reset</code></p>
    <p>
      Función:
      <ul>
        <li>Elimina todos los documentos de MongoDB</li>
        <li>Borra la tabla SQL en MySQL</li>
      </ul>
    </p>
    <p>Respuesta:</p>
    <pre>
{
  "mensaje": "Sistema reseteado correctamente",
  "mongo_docs_eliminados": 150,
  "mysql_rows_eliminadas": 150,
  "status": 200
}
    </pre>
  </div>

  <div class="box">
    <h3>🗄️ Bases de Datos</h3>

    <h4>📦 MongoDB (Staging)</h4>
    <ul>
      <li><strong>Base:</strong> rick_and_morty_staging</li>
      <li><strong>Colección:</strong> raw_characters</li>
      <li>Contiene los JSON crudos extraídos de la API.</li>
    </ul>

    <h4>🏛️ MySQL (Data Warehouse)</h4>
    <ul>
      <li><strong>Base:</strong> rick_and_morty_dw</li>
      <li><strong>Tabla:</strong> personajes_master</li>
    </ul>

    <table>
      <tr>
        <th>Columna</th>
        <th>Tipo</th>
      </tr>
      <tr>
        <td>id_personaje</td>
        <td>INTEGER (PK)</td>
      </tr>
      <tr>
        <td>nombre</td>
        <td>VARCHAR</td>
      </tr>
      <tr>
        <td>estado</td>
        <td>VARCHAR</td>
      </tr>
      <tr>
        <td>especie</td>
        <td>VARCHAR</td>
      </tr>
      <tr>
        <td>genero</td>
        <td>VARCHAR</td>
      </tr>
      <tr>
        <td>origen</td>
        <td>VARCHAR</td>
      </tr>
      <tr>
        <td>ubicacion</td>
        <td>VARCHAR</td>
      </tr>
      <tr>
        <td>imagen</td>
        <td>VARCHAR</td>
      </tr>
    </table>
  </div>

  <div class="box">
    <h3>🔁 Idempotencia</h3>
    <ul>
      <li><strong>Extract:</strong> Verifica si el personaje ya existe en MongoDB antes de insertarlo.</li>
      <li><strong>Transform/Load:</strong> Reemplaza la tabla SQL antes de cargar nuevos datos, evitando duplicados.</li>
    </ul>
  </div>

  <div class="box">
    <h3>🧪 Orden Correcto de Ejecución</h3>
    <ol>
      <li>DELETE <code>/api/v1/etl/reset</code></li>
      <li>POST <code>/api/v1/etl/extraer</code></li>
      <li>POST <code>/api/v1/etl/transformar</code></li>
    </ol>
  </div>

  <div class="box">
    <h3>📸 Evidencias Requeridas (PDF de entrega)</h3>
    <ul>
      <li>✔️ Swagger/Postman: ejecución exitosa de los 3 endpoints</li>
      <li>✔️ MongoDB: documentos cargados en <code>raw_characters</code></li>
      <li>✔️ MySQL/DBeaver: tabla <code>personajes_master</code> llena</li>
    </ul>
  </div>

  <div class="box">
    <h3>🎯 Consideraciones de Diseño</h3>
    <ul>
      <li>Arquitectura modular basada en MVC + Services</li>
      <li>Separación clara entre ingesta, transformación y persistencia</li>
      <li>Uso de variables de entorno para seguridad</li>
      <li>Pipeline reproducible y reiniciable</li>
    </ul>
  </div>

  <div class="box">
    <h3>🧠 Fuente de Datos</h3>
    <p>API pública: <a href="https://rickandmortyapi.com" target="_blank">https://rickandmortyapi.com</a></p>
  </div>

  <div class="box">
    <h3>✅ Estado del Proyecto</h3>
    <ul>
      <li>✔️ ETL completo funcional</li>
      <li>✔️ Endpoints documentados</li>
      <li>✔️ MongoDB + MySQL integrados</li>
      <li>✔️ Idempotencia implementada</li>
      <li>✔️ Listo para sustentación</li>
    </ul>
  </div>

</body>
</html>
