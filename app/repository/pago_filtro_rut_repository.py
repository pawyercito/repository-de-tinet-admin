# repository.py
from app.models.db.pago_filtro_rut_model_db import PagoFiltroRut
from app.repository.base_repository import BaseRepository

class PagoFiltroRutRepository(BaseRepository):
    def find_first_by_rut_cliente_and_fecha_fin_is_null(self, rut_cliente):
        return self.session.query(PagoFiltroRut).filter(
            PagoFiltroRut.rut_cliente == rut_cliente,
            PagoFiltroRut.fecha_fin.is_(None)
        ).first()

    def save(self, pago_filtro_rut):
        self.session.add(pago_filtro_rut)
        self.session.commit()
        self.session.refresh(pago_filtro_rut)
        return pago_filtro_rut
    
    

    
    