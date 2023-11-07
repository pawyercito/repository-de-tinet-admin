from app.use_case.configuracion_pago_online.eliminar_toda_configuracion_pago_online_use_case import EliminaConfiguracionPagoOnlineCompletaUseCase
class EliminaConfiguracionPagoOnlineCompletaController:
    def __init__(self, use_case: EliminaConfiguracionPagoOnlineCompletaUseCase):
        self.use_case = use_case

    def handle(self, id: int):
        result = self.use_case.execute(id)
        if result:
            return {"message": "Se elimino correctamente"}, 200
        else:
            return {"error": "No se pudo eliminar"}, 400