from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import composite

Base = declarative_base()

class ParametrosPago(Base):
    __tablename__ = 'PARAMETROS_PAGO'
    
    id_padre = Column(String, primary_key=True, name='ID_PADRE')
    id = Column(String, primary_key=True, name='ID')
    valor = Column(String, name='VALOR')
    descripcion = Column(String, name='DESCRIPCION')

    def to_dict(self):
        return {
            'id_padre': self.id_padre,
            'id': self.id,
            'valor': self.valor,
            'descripcion': self.descripcion
        }
