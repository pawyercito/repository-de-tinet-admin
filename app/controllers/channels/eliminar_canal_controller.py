from app.use_case.canales.eliminar_canal_use_case import EliminarCanalUseCase
from fastapi import HTTPException

from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

class EliminarCanalController:
    def __init__(self, eliminar_canal_use_case: EliminarCanalUseCase):
        self.eliminar_canal_use_case = eliminar_canal_use_case

    def eliminar_canal(self, canal_to: dict):
        try:
            response = self.eliminar_canal_use_case.eliminar_canal(canal_to)
            if response is None:
                return {"error": "No se recibió ninguna respuesta del método eliminar_canal"}
            return response
        except SQLAlchemyError as e:
            return {"error": f"Error de SQLAlchemy: {e}"}
        except HTTPException as e:
            return {"error": e.detail}
        except Exception as e:
            return {"error": str(e) or "Ocurrió un error desconocido"}
        
    
        