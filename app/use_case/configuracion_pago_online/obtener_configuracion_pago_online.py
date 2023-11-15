from app.repository.configuracion_pago_online_repository import ConfiguracionPagoOnlineRepository
from typing import Optional
from app.models.db.configuracion_pago_online_db_model import ConfiguracionPagoOnline
class ObtenerConfiguracionPagoOnlineUseCase:
    def __init__(self, repository: ConfiguracionPagoOnlineRepository):
        self.repository = repository

    def execute(self, id: int) -> Optional[ConfiguracionPagoOnline]:
        return self.repository.listado_pago(id)