from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date, time
from typing import Literal

app = FastAPI()

class Reserva(BaseModel):
    id_reserva: int = Field(..., gt=0)
    id_sala: int = Field(..., gt=0)
    id_usuario: int = Field(..., gt=0)
    fecha: date
    hora_inicio: time
    hora_fin: time
    personas: int = Field(..., gt=0, le=100)
    estado: Literal["Activa", "Cancelada", "Finalizada"]

    class Config:
        schema_extra = {
            "example": {
                "id_reserva": 1,
                "id_sala": 101,
                "id_usuario": 2001,
                "fecha": "2026-03-10",
                "hora_inicio": "08:00:00",
                "hora_fin": "10:00:00",
                "personas": 20,
                "estado": "Activa"
            }
        }