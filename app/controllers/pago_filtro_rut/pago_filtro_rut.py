# controller.py
from fastapi import HTTPException
from app.use_case.pago_filtro_rut.pago_filtro_rut_use_case import PagoFiltroRutUseCase

class PagoFiltroRutController:
    def __init__(self, use_case: PagoFiltroRutUseCase):
        self.use_case = use_case

    def procesar_pago_filtro_rut(self, rut_cliente, nombre_cliente, motivo):
        return self.use_case.procesar_pago_filtro_rut(rut_cliente, nombre_cliente, motivo)
    
        

    
