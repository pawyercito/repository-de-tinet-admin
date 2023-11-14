from app.repository.pago_filtro_rut_repository import PagoFiltroRutRepository
from app.models.pago_filtro_rut_to_model import PagoFiltroRutRequest
import logging
class ListarPagoFiltroRutsUseCase:
    def __init__(self, repository: PagoFiltroRutRepository):
        self.repository = repository

    def execute(self):
        pagos_filtro_rut = self.repository.obtener_todos_los_pagos_filtro_rut()
        logging.info(f"Pagos filtro rut obtenidos de la consulta: {pagos_filtro_rut}")
        if pagos_filtro_rut is None:
            raise Exception("No se encontraron pagos filtro Rut")
        return [PagoFiltroRutRequest(**pago_filtro_rut).dict() for pago_filtro_rut in pagos_filtro_rut]