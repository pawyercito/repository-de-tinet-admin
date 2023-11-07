from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import composite

Base = declarative_base()

class PagoFiltroRut(Base):
    __tablename__ = 'PAGO_FILTRO_RUT'
    
    rut_cliente = Column(String, primary_key=True, name='rut_cliente')
    fechaInicio = Column(DateTime,primary_key=True, name='fecha_inicio')
    nombre_cliente = Column(String, name='nombre_cliente')
    motivo = Column(String, name='motivo')
    fecha_fin = Column(DateTime, name='fecha_fin')
