# use_case.py
from app.repository.pago_filtro_rut_repository import PagoFiltroRutRepository
from app.models.db.pago_filtro_rut_model_db import PagoFiltroRut
from app.models.pago_filtro_rut_to_model import PagoFiltroRutRequest
from datetime import datetime

class PagoFiltroRutUseCase:
    def __init__(self, repository: PagoFiltroRutRepository):
        self.repository = repository

    def execute(self, request: PagoFiltroRutRequest):
        existing_rut = self.repository.find_first_by_rut_cliente_and_fecha_fin_is_null(request.rut_cliente)

        if existing_rut is not None:
            existing_rut.fecha_fin = datetime.now()
            self.repository.update(existing_rut)

        pago_filtro_rut = PagoFiltroRut(
            rut_cliente=request.rut_cliente,
            fecha_inicio=request.fecha_inicio,
            nombre_cliente=request.nombre_cliente,
            motivo=request.motivo,
            fecha_fin=request.fecha_fin
        )
        self.repository.create(pago_filtro_rut)
        return {"message": "Operation successful"}
    



    
