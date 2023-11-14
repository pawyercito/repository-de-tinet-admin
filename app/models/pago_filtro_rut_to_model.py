from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PagoFiltroRutRequest(BaseModel):
    rut_cliente: str
    fecha_inicio: datetime
    nombre_cliente: str
    motivo: str
    fecha_fin: Optional[datetime] 