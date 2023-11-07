from app.models.canales_model import Canales
from app.repository.canales_repository import CanalesRepository

import logging

class ListarCanalesUseCase:
    def __init__(self, canales_repository: CanalesRepository):
        self.canales_repository = canales_repository

    def listar_canales(self):
        canales = self.canales_repository.obtener_todos_los_canales()
        logging.info(f"Canales obtenidos de la base de datos: {canales}")
        if canales is None:
            raise Exception("No se encontraron canales")
        return [Canales(**canal).dict() for canal in canales]