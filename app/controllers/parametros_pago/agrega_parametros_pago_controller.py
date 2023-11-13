from app.use_case.parametros_pago.agrega_parametros_pago_use_case import AgregaParametrosPagoUseCase
from app.models.parametros_pago_model import ParametrosPago

class AgregaParametrosPagoController:
    def __init__(self, parametros_pago_use_case: AgregaParametrosPagoUseCase):
        self.parametros_pago_use_case = parametros_pago_use_case

    def agrega_parametros(self, parametros_pago_to: dict):
        try:
            parametros_pago_data={
                "id_padre": parametros_pago_to.get("id_padre"),
                "id": parametros_pago_to.get("id"),
                "valor": parametros_pago_to.get("valor"),
                "descripcion": parametros_pago_to.get("descripcion")
            }
            response = self.parametros_pago_use_case.agrega_parametros(parametros_pago_data)
            return response
        except Exception as e:
            return {"error": str(e)}





