# app/use_case/agrega_parametros_pago_use_case.py

from app.repository.parametros_pago_repository import ParametrosPagoRepository
from app.models.parametros_pago_model import ParametrosPago
from app.models.parametros_pago_key_model import ParametrosPagoKey

class AgregaParametrosPagoUseCase:
    def __init__(self, repo: ParametrosPagoRepository):
        self.repo = repo

    def agrega_parametros(self, parametros_pago_to):
        parametros_pago_key = ParametrosPagoKey(id=parametros_pago_to.id, id_padre=parametros_pago_to.id_padre)
        parametros_pago = ParametrosPago(claves=parametros_pago_key, descripcion=parametros_pago_to.descripcion, valor=parametros_pago_to.valor)
        
        if self.valida_campos_parametros(parametros_pago):
            if not self.repo.exists(parametros_pago.claves):
                try:
                    self.repo.save(parametros_pago)
                    return "SE_AGREGO_CORRECTAMENTE"
                except Exception as e:
                    return "NO_SE_PUDO_AGREGAR"
            else:
                return "EL_REGISTRO_YA_EXISTE"
        else:
            return "parametros"

    def valida_campos_parametros(self, parametros_pago):
        # logica de validacion de parametros
        def valida_campos_parametros(self, parametros_pago):
            if not parametros_pago.claves.id:
                return False
            if not parametros_pago.claves.id_padre:
                return False
            if not parametros_pago.descripcion:
                return False
            if not parametros_pago.valor:
                return False
            return True
        