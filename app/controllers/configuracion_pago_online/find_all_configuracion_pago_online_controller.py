from app.use_case.configuracion_pago_online.find_all_configuracion_pago_online_use_case import ListadoConfiguracionPagoOnlineUseCase

class ListadoConfiguracionPagoOnlineController:
    def __init__(self, use_case: ListadoConfiguracionPagoOnlineUseCase):
        self.use_case = use_case

    def handle(self):
        result = self.use_case.execute()
        if result is None:
            return {"error": "No se encontraron registros."}, 400
        else:
            return result, 200