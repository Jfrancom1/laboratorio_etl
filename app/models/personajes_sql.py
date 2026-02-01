from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Personaje(Base):
    __tablename__ = "personajes_master"

    id_personaje = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    estado = Column(String(50))
    especie = Column(String(50))
    genero = Column(String(50))
    origen = Column(String(100))
    ubicacion = Column(String(100))
    imagen = Column(String(255))
