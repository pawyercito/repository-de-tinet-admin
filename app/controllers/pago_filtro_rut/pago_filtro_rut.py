# controller.py
from fastapi import HTTPException
from app.use_case.pago_filtro_rut.pago_filtro_rut_use_case import PagoFiltroRutUseCase

class PagoFiltroRutController:
    def __init__(self, use_case: PagoFiltroRutUseCase):
        self.use_case = use_case

    def procesar_pago_filtro_rut(self, rut_cliente: str, nombre_cliente: str, motivo: str):
        try:
            pago_filtro_rut = self.use_case.execute(rut_cliente, nombre_cliente, motivo)
            return pago_filtro_rut
        except HTTPException as e:
            return {"error": e.detail}

    
        

    
