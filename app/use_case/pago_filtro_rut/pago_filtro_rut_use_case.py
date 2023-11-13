# use_case.py
from app.repository.pago_filtro_rut_repository import PagoFiltroRutRepository
from app.models.pago_filtro_rut_to_model import PagoFiltroRutDTO
from app.models.db.pago_filtro_rut_model_db import PagoFiltroRut
from datetime import datetime

class PagoFiltroRutUseCase:
    def __init__(self, repo: PagoFiltroRutRepository):
        self.repo = repo

    def execute(self, rut_cliente: str, nombre_cliente: str, motivo: str):
        existing = self.repo.find_first_by_rut_and_fecha_fin_is_null(rut_cliente)
        if existing:
            existing.fecha_fin = datetime.now()
            self.repo.save(existing)
        new_pago_filtro_rut = PagoFiltroRut(rut_cliente=rut_cliente, nombre_cliente=nombre_cliente, motivo=motivo, fecha_inicio=datetime.now())
        saved_pago_filtro_rut = self.repo.save(new_pago_filtro_rut)
        if not saved_pago_filtro_rut:
            raise Exception("Failed to save PagoFiltroRut")
        return saved_pago_filtro_rut


    
