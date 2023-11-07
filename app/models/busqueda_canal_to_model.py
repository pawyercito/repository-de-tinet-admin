from pydantic import BaseModel

class BusquedaCanalTO(BaseModel):
    producto: int
    id_convenio: str
    tipo_origen: int
    tipo_seguro: int