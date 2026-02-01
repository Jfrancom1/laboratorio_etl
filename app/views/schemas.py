from pydantic import BaseModel, Field

class ExtractRequest(BaseModel):
    cantidad: int = Field(..., gt=0, description="Cantidad de registros a extraer")

class GenericResponse(BaseModel):
    mensaje: str
    status: int