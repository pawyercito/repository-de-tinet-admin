# use_case.py
from app.repository.pago_filtro_rut_repository import PagoFiltroRutRepository
from app.models.db.pago_filtro_rut_model_db import PagoFiltroRut
from datetime import datetime

class PagoFiltroRutUseCase:
    def __init__(self, repository: PagoFiltroRutRepository):
        self.repository = repository

    def pago_filtro_rut(self, rut, nombre, motivo):
        existing_record = self.repository.find_by_rut(rut)
        if existing_record:
            existing_record.fecha_fin = datetime.now()
        pago_filtro_rut = PagoFiltroRut(rut_cliente=rut, nombre_cliente=nombre, motivo=motivo)
        self.repository.create(pago_filtro_rut)
