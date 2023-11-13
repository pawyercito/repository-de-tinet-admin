# app/use_case/elimina_parametros_pago_use_case.py

from app.repository.parametros_pago_repository import ParametrosPagoRepository

from sqlalchemy.exc import SQLAlchemyError

class EliminaParametrosPagoUseCase:
    def __init__(self, parametros_pago_repository: ParametrosPagoRepository):
        self.parametros_pago_repository = parametros_pago_repository

    def delete(self, parametros_pago_data: dict):
        try:
            response = self.parametros_pago_repository.delete(**parametros_pago_data)
            if response is None:
                return {"error": "No se recibió ninguna respuesta del método delete en ParametrosPagoRepository"}
            return response
        except SQLAlchemyError as e:
            return {"error": f"Error de SQLAlchemy: {e}"}
        except Exception as e:
            return {"error": str(e) or "Ocurrió un error desconocido"}

