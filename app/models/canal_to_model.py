from typing import List
from pydantic import BaseModel
from datetime import datetime

class CanalesTO(BaseModel):
    idCanal: int
    passwordCanal: str
    idEmpresa: int
    descripcion: str
    tipoProducto: int
    tipoOrigen: int
    producto: int
    idConvenio: str
    tipoSeguro: int