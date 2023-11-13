# app/use_case/agrega_parametros_pago_use_case.py

from app.repository.parametros_pago_repository import ParametrosPagoRepository

class AgregaParametrosPagoUseCase:
    def __init__(self, parametros_pago_repository: ParametrosPagoRepository):
        self.parametros_pago_repository = parametros_pago_repository

    def agrega_parametros(self, parametros_data: dict):
        #Verifica si el parametro de pago ya existe antes de intentar guardar en la base de datos
        if self.parametros_pago_repository.exists(**parametros_data):
            raise Exception("El parametro de pago ya existe y no se puede agregar nuevamente.")
        
        return self.parametros_pago_repository.save(parametros_data)
       