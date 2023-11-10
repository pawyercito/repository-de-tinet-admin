from typing import List
from pydantic import BaseModel
from datetime import datetime

class Canales(BaseModel):
    idCanal: int
    passwordCanal: str
    idEmpresa: int
    descripcion: str
    tipoProducto: int
    tipoOrigen: int
    producto: str
    idConvenio: str
    tipoSeguro: int
