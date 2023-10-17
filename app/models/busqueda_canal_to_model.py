from typing import List
from pydantic import BaseModel
from datetime import datetime

class BusquedaCanalTO(BaseModel):
    producto: str
    id_convenio: str
    tipo_origen: str
    tipo_seguro: str

class CanalesKey(BaseModel):
    producto: int
    idConvenio: str
    tipoOrigen: int
    tipoSeguro: int    

class Canales(BaseModel):
    claves: CanalesKey
    idCanal: int
    passwordCanal: str
    idEmpresa: int
    descripcion: str
    tipoProducto: int

class CanalTO(BaseModel):
    producto: int
    idConvenio: str
    tipoOirgen: int
    tipoSeguro: int
    idCanal: int
    passwordCanal: str
    idEmpresa: int
    descripcion: str
    tipoProducto: int    

class ParametrosPagoKey(BaseModel):
    idPadre: str
    id: str

class ParametrosPago(BaseModel):
    claves: ParametrosPagoKey
    valor: str
    descripcion: str

class ParametrosPagoTO(BaseModel):
    idPadre: str
    id: str
    valor: str
    descripcion: str

class PagoFiltroRutTO(BaseModel):
    rutCliente: str
    nombreCliente: str
    motivo: str
    fechaInicio: str
    fechaFin: str

class ConfiguracionPagoOnlineTO(BaseModel):
    id: int
    glosa: str
    valor: str
    deffecdate: str
    dnulldate: str

class ConfiguracionPagoOnline(BaseModel):
    id: int
    glosa: str
    valor: str
    deffecdate: datetime
    dnulldate: datetime                        




 

    