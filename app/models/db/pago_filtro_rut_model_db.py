from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import composite
from datetime import datetime


Base = declarative_base()

class PagoFiltroRut(Base):
    __tablename__ = 'PAGO_FILTRO_RUT'
    
    rut_cliente = Column(String, primary_key=True, name='rut_cliente')
    fecha_inicio = Column(DateTime,primary_key=True, name='fecha_inicio')
    nombre_cliente = Column(String, name='nombre_cliente')
    motivo = Column(String, name='motivo')
    fecha_fin = Column(DateTime, name='fecha_fin')

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat() if isinstance(v, datetime) else v,
        }

    def to_dict(self):
        return {
            'rut_cliente': self.rut_cliente,
            'nombre_cliente': self.nombre_cliente,
            'motivo': self.motivo,
            'fecha_inicio': self.fecha_inicio.isoformat() if self.fecha_inicio else None,
            'fecha_fin': self.fecha_fin.isoformat() if self.fecha_fin else None
        }
    


