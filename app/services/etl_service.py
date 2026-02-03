import requests
import pandas as pd
from app.database import mongo_collection, engine
from app.models.personajes_sql import Base, Personaje

# ---------- ENDPOINT A: EXTRACT ----------
def extract_characters_service(cantidad: int):
    url = "https://rickandmortyapi.com/api/character"
    params = {"page": 1}
    total_guardados = 0

    while total_guardados < cantidad:
        response = requests.get(url, params=params)
        data = response.json()
        results = data.get("results", [])

        for character in results:
            if total_guardados >= cantidad:
                break

            character_id = character["id"]

            # Idempotencia: evitar duplicados
            if mongo_collection.find_one({"id": character_id}):
                continue

            mongo_collection.insert_one(character)
            total_guardados += 1

        if data["info"]["next"] is None:
            break

        params["page"] += 1

    return {
        "mensaje": "Datos extraídos exitosamente",
        "registros_guardados": total_guardados,
        "fuente": "Rick & Morty API",
        "status": 201
    }

### Se crea la funcion transform_load_service ###
def transform_load_service():
    # 1. Se extraen los datos desde MongoDB
    documents = list(mongo_collection.find({}, {"_id": 0}))

    if not documents:
        return {
            "mensaje": "No hay datos para procesar",
            "registros_procesados": 0,
            "tabla_destino": "personajes_master",
            "status": 200
        }

    # 2. Se transforman con Pandas
    df = pd.json_normalize(documents)