from app.models.configuracion_pago_online_to_model import ConfiguracionPagoOnlineTO
from app.use_case.configuracion_pago_online.configuracion_pago_online_use_case import AgregarConfiguracionPagoOnlineUseCase

class AgregarConfiguracionPagoOnlineController:
    def __init__(self, use_case: AgregarConfiguracionPagoOnlineUseCase):
        self.use_case = use_case

    def handle(self, configuracion_pago_online_to: ConfiguracionPagoOnlineTO, id: int):
        result = self.use_case.execute(configuracion_pago_online_to, id)
        if result is None:
            return {"error": "Bad Request"}, 400
        else:
            return {"message": "Se agrego correctamente"}, 200