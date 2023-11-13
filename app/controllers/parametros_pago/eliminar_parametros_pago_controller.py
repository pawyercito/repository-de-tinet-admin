# app/controllers/parametros_pago/elimina_parametros_pago_controller.py

from app.use_case.parametros_pago.elimina_parametros_pago_use_case import EliminaParametrosPagoUseCase
from app.models.parametros_pago_to_model import ParametrosPagoTO

from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

class EliminaParametrosPagoController:
    def __init__(self, eliminar_parametros_pago_use_case: EliminaParametrosPagoUseCase):
        self.eliminar_parametros_pago_use_case = eliminar_parametros_pago_use_case

    def elimina_parametros(self, parametros_pago_to: dict):
        try:
            response = self.eliminar_parametros_pago_use_case.delete(parametros_pago_to)
            if response is None:
                return {"error": "No se recibió ninguna respuesta del método delete en ParametrosPagoRepository"}
            return response
        except SQLAlchemyError as e:
            return {"error": f"Error de SQLAlchemy: {e}"}
        except HTTPException as e:
            return {"error": e.detail}
        except Exception as e:
            return {"error": str(e) or "Ocurrió un error desconocido"}

        