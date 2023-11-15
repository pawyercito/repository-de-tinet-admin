from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class ConfiguracionPagoOnline(Base):
    __tablename__ = 'TBL_PAGO_CONFIGURACION'

    id = Column(Integer, primary_key=True, autoincrement=False, index=True, name='NID')
    glosa = Column(String, name='SGLOSA')
    valor = Column(String, name='SVALOR')
    deffecdate: datetime = Column(DateTime, default=func.current_timestamp(), name='DEFFECDATE')
    dnulldate: datetime = Column(DateTime, name='DNULLDATE')


    
    def to_dict(self):

 
        
        return {
            'id': self.id,
            'glosa': self.glosa,
            'valor': self.valor,
            'deffecdate': self.deffecdate.strftime("%m/%d/%Y, %H:%M:%S") if self.deffecdate else None,
            'dnulldate': self.dnulldate.strftime("%m/%d/%Y, %H:%M:%S") if self.dnulldate else None 
        }