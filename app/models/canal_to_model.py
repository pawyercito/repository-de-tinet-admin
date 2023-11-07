from typing import List
from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel

class CanalTO(BaseModel):
    producto: int
    idConvenio: str
    tipoOrigen: int
    tipoSeguro: int
    idCanal: int
    passwordCanal: str
    idEmpresa: int
    descripcion: str
    tipoProducto: int