from fastapi import FastAPI
from app.controllers.etl_controller import router as etl_router

app = FastAPI(title="Laboratorio ETL - Rick & Morty")

app.include_router(etl_router, prefix="/api/v1/etl")