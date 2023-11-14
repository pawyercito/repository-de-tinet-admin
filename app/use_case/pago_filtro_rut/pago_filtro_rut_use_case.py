# use_case.py
from app.repository.pago_filtro_rut_repository import PagoFiltroRutRepository
from app.models.db.pago_filtro_rut_model_db import PagoFiltroRut
from datetime import datetime

class PagoFiltroRutUseCase:
    def __init__(self, repository: PagoFiltroRutRepository):
        self.repository = repository

    def procesar_pago_filtro_rut(self, rut_cliente, nombre_cliente, motivo):
        filtro_rut = self.repository.find_first_by_rut_cliente_and_fecha_fin_is_null(rut_cliente)

        if filtro_rut:
            filtro_rut.fecha_fin = datetime.utcnow()
            self.repository.save(filtro_rut)

        new_pago_filtro_rut = PagoFiltroRut(
            rut_cliente=rut_cliente,
            nombre_cliente=nombre_cliente,
            motivo=motivo,
        )

        result = self.repository.save(new_pago_filtro_rut)
        return result
    


    
