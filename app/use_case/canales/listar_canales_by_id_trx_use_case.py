from app.models.canales_model import Canales
from app.repository.canales_repository import CanalesRepository

class ListarCanalesByIdTrxUseCase:
    def __init__(self, canales_repository: CanalesRepository):
        self.canales_repository = canales_repository

    def listar_canales_by_id_trx(self, id_trx, nro_orden):
        canales = self.canales_repository.buscar_canales_por_id_trx_y_nro_orden(id_trx, nro_orden)
        if canales is None:
            raise Exception("No se encontraron canales")
        return [Canales(**canal).dict() for canal in canales]