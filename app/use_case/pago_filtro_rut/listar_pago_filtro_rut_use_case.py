from app.repository.pago_filtro_rut_repository import PagoFiltroRutRepository

class ListarPagoFiltroRutsUseCase:
    def __init__(self, repository: PagoFiltroRutRepository):
        self.repository = repository

    def execute(self):
        return self.repository.find_all()