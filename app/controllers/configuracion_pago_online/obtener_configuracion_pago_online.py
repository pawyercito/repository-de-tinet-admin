from app.use_case.configuracion_pago_online.obtener_configuracion_pago_online import ObtenerConfiguracionPagoOnlineUseCase

class ObtenerConfiguracionPagoOnlineController:
    def __init__(self, use_case: ObtenerConfiguracionPagoOnlineUseCase):
        self.use_case = use_case

    def handle(self, id: int):
        result = self.use_case.execute(id)
        if result is None:
            return {"error": "No se encontraron registros para el ID proporcionado."}, 400
        else:
            return result, 200