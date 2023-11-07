from typing import List
from pydantic import BaseModel
from datetime import datetime
from app.models.parametros_pago_key_model import ParametrosPagoKey

class ParametrosPago(BaseModel):
    claves: ParametrosPagoKey
    valor: str
    descripcion: str

    