from app.repository.configuracion_pago_online_repository import ConfiguracionPagoOnlineRepository

class EliminaConfiguracionPagoOnlineUseCase:
    def __init__(self, repository: ConfiguracionPagoOnlineRepository):
        self.repository = repository

    def execute(self, id: int):
        return self.repository.eliminar_configuracion_pago(id)