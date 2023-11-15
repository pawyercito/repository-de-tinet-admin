from pydantic import BaseModel
from datetime import datetime

class ListarCanalesByIdTrxNroOrdenTO(BaseModel):
    idTrx: int
    nroOrden: int