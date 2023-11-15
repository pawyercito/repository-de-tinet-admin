from pydantic import BaseModel
from datetime import datetime

class ConfiguracionPagoOnlineTO(BaseModel):
    glosa: str
    valor: str
    deffecdate: datetime
    dnulldate: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat() if isinstance(v, datetime) else v,
        }