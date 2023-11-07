from pydantic import BaseModel

class ParametrosPagoTO(BaseModel):
    idPadre: str
    id: str
    valor: str
    descripcion: str