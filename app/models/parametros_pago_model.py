from typing import List
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ParametrosPago(BaseModel):
    id_padre: str
    id: str
    valor: str
    descripcion: Optional[str] = None

    