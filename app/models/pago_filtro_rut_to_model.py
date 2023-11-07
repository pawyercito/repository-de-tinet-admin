from pydantic import BaseModel

class PagoFiltroRutTO(BaseModel):
    rutCliente: str
    nombreCliente: str
    motivo: str
    fechaInicio: str
    fechaFin: str