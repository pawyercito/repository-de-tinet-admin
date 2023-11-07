from app.repository.configuracion_pago_online_repository import ConfiguracionPagoOnlineRepository

class ListadoConfiguracionPagoOnlineUseCase:
    def __init__(self, repository: ConfiguracionPagoOnlineRepository):
        self.repository = repository

    def execute(self):
        return self.repository.find_all()