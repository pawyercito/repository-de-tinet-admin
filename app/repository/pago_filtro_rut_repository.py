# repository.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.db.pago_filtro_rut_model_db import PagoFiltroRut
from sqlalchemy.orm.session import Session
from app.repository.base_repository import BaseRepository

class PagoFiltroRutRepository(BaseRepository):

    def create(self, pago_filtro_rut):
        db = self.SessionLocal()
        db.add(pago_filtro_rut)
        db.commit()
        db.refresh(pago_filtro_rut)
        db.close()

    def find_by_rut(self, rut):
        db = self.SessionLocal()
        result = db.query(PagoFiltroRut).filter(PagoFiltroRut.rut_cliente == rut).first()
        db.close()
        return result
    
    def find_all(self):
        return self.db.query(PagoFiltroRut).all()
