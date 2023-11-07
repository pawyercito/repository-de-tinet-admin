# app/controllers/parametros_pago/elimina_parametros_pago_controller.py

from app.use_case.parametros_pago.elimina_parametros_pago_use_case import EliminaParametrosPagoUseCase
from app.models.parametros_pago_to_model import ParametrosPagoTO

class EliminaParametrosPagoController:
    def __init__(self, use_case: EliminaParametrosPagoUseCase):
        self.use_case = use_case

    def elimina_parametros(self, parametros_pago_to: ParametrosPagoTO):
        return self.use_case.elimina_parametros(parametros_pago_to)