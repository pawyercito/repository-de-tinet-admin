from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Canales(Base):
    __tablename__ = "CANALES"

    idCanal = Column(Integer, primary_key=True, index=True, name="ID_CANAL")
    passwordCanal = Column(String, name="PASSWORDCANAL")
    idEmpresa = Column(Integer, name="ID_EMPRESA")
    descripcion = Column(String, name="DESCRIPCION")
    tipoProducto = Column(Integer, name="TIPO_PRODUCTO")
    tipoOrigen = Column(Integer,primary_key=True, index=True, name = "TIPO_ORIGEN")
    producto = Column(Integer, name = "PRODUCTO" )
    idConvenio = Column(String,primary_key=True, index=True,  name = "ID_CONVENIO")
    tipoSeguro = Column(Integer, primary_key=True, index=True, name = "TIPO_SEGURO")

    def to_dict(self):
        return {
            'idCanal': self.idCanal,
            'passwordCanal': self.passwordCanal,
            'idEmpresa': self.idEmpresa,
            'descripcion': self.descripcion,
            'tipoProducto': self.tipoProducto,
            'tipoOrigen': self.tipoOrigen,
            'producto': self.producto,
            'idConvenio': self.idConvenio,
            'tipoSeguro': self.tipoSeguro
        }