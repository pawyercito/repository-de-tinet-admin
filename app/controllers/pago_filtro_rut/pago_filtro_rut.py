# controller.py
from fastapi import HTTPException
from app.use_case.pago_filtro_rut.pago_filtro_rut_use_case import PagoFiltroRutUseCase
from app.models.pago_filtro_rut_to_model import PagoFiltroRutRequest

class PagoFiltroRutController:
    def __init__(self, use_case: PagoFiltroRutUseCase):
        self.use_case = use_case

    def handle(self, request: PagoFiltroRutRequest):
        return self.use_case.execute(request)

    
