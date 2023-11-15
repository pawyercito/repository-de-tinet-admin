from app.use_case.configuracion_pago_online.find_all_configuracion_pago_online_use_case import ListadoConfiguracionPagoOnlineUseCase
from typing import Optional
from app.models.db.configuracion_pago_online_db_model import ConfiguracionPagoOnline
class ListadoConfiguracionPagoOnlineController:
    def __init__(self, use_case: ListadoConfiguracionPagoOnlineUseCase):
        self.use_case = use_case

    def handle(self):
        result : Optional[list [ConfiguracionPagoOnline]] = self.use_case.execute()
        if result is None:
            return {"error": "No se encontraron registros."}, 400
        else:
            return [r.to_dict() for r in result], 200
            