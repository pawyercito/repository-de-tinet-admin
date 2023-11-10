from fastapi import HTTPException
from app.repository.canales_repository import CanalesRepository

from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

class EliminarCanalUseCase:
    def __init__(self, canales_repository: CanalesRepository):
        self.canales_repository = canales_repository

    def eliminar_canal(self, canal_data: dict):
        try:
            response = self.canales_repository.eliminar_canal(**canal_data)
            if response is None:
                return {"error": "No se recibió ninguna respuesta del método eliminar_canal en CanalesRepository"}
            return response
        except SQLAlchemyError as e:
            return {"error": f"Error de SQLAlchemy: {e}"}
        except Exception as e:
            return {"error": str(e) or "Ocurrió un error desconocido"}