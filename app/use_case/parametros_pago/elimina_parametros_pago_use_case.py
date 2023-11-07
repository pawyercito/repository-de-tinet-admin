# app/use_case/elimina_parametros_pago_use_case.py

from app.repository.parametros_pago_repository import ParametrosPagoRepository
from app.models.parametros_pago_model import ParametrosPago
from app.models.parametros_pago_key_model import ParametrosPagoKey

class EliminaParametrosPagoUseCase:
    def __init__(self, repo: ParametrosPagoRepository):
        self.repo = repo

    def elimina_parametros(self, parametros_pago_to):
        parametros_pago_key = ParametrosPagoKey(id=parametros_pago_to.id, id_padre=parametros_pago_to.id_padre)
        parametros_pago = ParametrosPago(claves=parametros_pago_key, descripcion=parametros_pago_to.descripcion, valor=parametros_pago_to.valor)
        
        if self.valida_campos_parametros(parametros_pago):
            if self.repo.exists(parametros_pago.claves):
                try:
                    self.repo.delete(parametros_pago.claves)
                    return "SE_ELIMINO_CORRECTAMENTE"
                except Exception as e:
                    return "NO_SE_PUDO_ELIMINAR"
            else:
                return "El registro no existe"
        else:
            return ""
