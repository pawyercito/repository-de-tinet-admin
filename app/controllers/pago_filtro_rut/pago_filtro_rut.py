# controller.py
from fastapi import HTTPException
from app.use_case.pago_filtro_rut.pago_filtro_rut_use_case import PagoFiltroRutUseCase

class PagoFiltroRutController:
    def __init__(self, use_case: PagoFiltroRutUseCase):
        self.use_case = use_case

    def pago_filtro_rut(self, rut, nombre, motivo):
        if not rut:
            raise HTTPException(status_code=400, detail="RutCliente is required")
        self.use_case.pago_filtro_rut(rut, nombre, motivo)
