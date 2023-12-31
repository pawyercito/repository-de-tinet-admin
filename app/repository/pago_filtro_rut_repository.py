# repository.py
from app.models.db.pago_filtro_rut_model_db import PagoFiltroRut
from app.repository.base_repository import BaseRepository
from sqlalchemy import and_
import logging
# En tu archivo repository.py

class PagoFiltroRutRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

    def find_first_by_rut_cliente_and_fecha_fin_is_null(self, rut_cliente):
        return self.session.query(PagoFiltroRut).filter(
            and_(PagoFiltroRut.rut_cliente == rut_cliente, PagoFiltroRut.fecha_fin.is_(None))
        ).first()

    def create(self, pago_filtro_rut: PagoFiltroRut):
        self.session.add(pago_filtro_rut)
        self.session.commit()
        return pago_filtro_rut
    
    def update(self, pago_filtro_rut: PagoFiltroRut):
        self.session.commit()
        return pago_filtro_rut
    
    def obtener_todos_los_pagos_filtro_rut(self):
        pago_filtro_rut = self.session.query(PagoFiltroRut).all()
        logging.info(f"Pagos filtro rut obtenidos de la consulta: {pago_filtro_rut}")
        if pago_filtro_rut is None:
            return None
        return [pago_filtro_rut.__dict__ for pago_filtro_rut in pago_filtro_rut]
    
    
        
        
    

    


    
    