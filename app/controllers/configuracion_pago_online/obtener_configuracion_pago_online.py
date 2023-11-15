from app.use_case.configuracion_pago_online.obtener_configuracion_pago_online import ObtenerConfiguracionPagoOnlineUseCase
from datetime import datetime
from typing import Optional
from app.models.db.configuracion_pago_online_db_model import ConfiguracionPagoOnline
from sqlalchemy.orm import class_mapper

class ObtenerConfiguracionPagoOnlineController:
    def __init__(self, use_case: ObtenerConfiguracionPagoOnlineUseCase):
        self.use_case = use_case

    def handle(self, id: int):
        result : Optional[ConfiguracionPagoOnline] = self.use_case.execute(id)

        def object_as_dict(obj):
            return {c.key: getattr(obj, c.key)
                    for c in class_mapper(obj.__class__).columns}
        
        if result is None:
            return {"error": "No se encontraron registros para el ID proporcionado."}, 400
        else:
    
            return result.to_dict(), 200