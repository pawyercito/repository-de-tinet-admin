from pydantic import BaseModel
from datetime import datetime

class ConfiguracionPagoOnlineTO(BaseModel):
    id: int
    glosa: str
    valor: str
    deffecdate: datetime
    dnulldate: datetime