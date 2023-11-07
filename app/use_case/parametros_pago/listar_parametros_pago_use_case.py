from app.repository.parametros_pago_repository import ParametrosPagoRepository

class ListarParametrosUseCase:
    def __init__(self, repository: ParametrosPagoRepository):
        self.repository = repository

    def listar_parametros(self):
        return self.repository.listar_parametros()