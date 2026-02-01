from fastapi import APIRouter, status
from app.views.schemas import ExtractRequest
from app.services.etl_service import (
    extract_characters_service,
    transform_load_service,
    reset_system_service
)

router = APIRouter()

@router.post("/extraer", status_code=status.HTTP_201_CREATED)
def extract_characters(request: ExtractRequest):
    return extract_characters_service(request.cantidad)

@router.post("/transformar", status_code=status.HTTP_200_OK)
def transform_and_load():
    return transform_load_service()

@router.delete("/reset", status_code=status.HTTP_200_OK)
def reset_system():
    return reset_system_service()