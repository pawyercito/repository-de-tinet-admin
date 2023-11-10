from typing import List
from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel

class CanalTO(BaseModel):
    idCanal: int
    producto: int
    idConvenio: str
    tipoOrigen: int
    tipoSeguro: int
    passwordCanal: str
    idEmpresa: int
    descripcion: str
    tipoProducto: int