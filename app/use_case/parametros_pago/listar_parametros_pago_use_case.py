from app.repository.parametros_pago_repository import ParametrosPagoRepository
import logging
from app.models.parametros_pago_model import ParametrosPago
class ListarParametrosUseCase:
    def __init__(self, parametros_pago_repository: ParametrosPagoRepository):
        self.parametros_pago_repository = parametros_pago_repository

    def listar_parametros(self):
        parametros = self.parametros_pago_repository.listar_parametros()
        logging.info(f"Parametros obtenidos de manera correcta")
        if parametros is None:
            raise Exception("No se encontraron parametros")
        return [ParametrosPago(**parametro).dict() for parametro in parametros]