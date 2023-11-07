from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class ConfiguracionPagoOnline(Base):
    __tablename__ = 'TBL_PAGO_CONFIGURACION'

    id = Column(Integer, primary_key=True, index=True, name='NID')
    glosa = Column(String, name='SGLOSA')
    valor = Column(String, name='SVALOR')
    deffecdate = Column(DateTime, default=func.current_timestamp(), name='DEFFECDATE')
    dnulldate = Column(DateTime, name='DNULLDATE')