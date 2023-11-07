from app.use_case.parametros_pago.agrega_parametros_pago_use_case import AgregaParametrosPagoUseCase
from app.models.parametros_pago_to_model import ParametrosPagoTO

class AgregaParametrosPagoController:
    def __init__(self, use_case: AgregaParametrosPagoUseCase):
        self.use_case = use_case

    def agrega_parametros(self, parametros_pago_to: ParametrosPagoTO):
        return self.use_case.agrega_parametros(parametros_pago_to)





