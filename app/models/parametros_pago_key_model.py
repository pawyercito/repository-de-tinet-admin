from typing import List
from pydantic import BaseModel
from datetime import datetime

class ParametrosPagoKey(BaseModel):
    idPadre: str
    id: str