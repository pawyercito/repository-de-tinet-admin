from app.repository.canales_repository import CanalesRepository
from app.models.canales_model import Canales

class EliminarCanalUseCase:
    def __init__(self, repository: CanalesRepository):
        self.repository = repository

    def eliminar_canal(self, id):
        if self.repository.existe_canal(id):
            self.repository.eliminar_canal(id)
            return "Se eliminó correctamente"
        else:
            return "El registro no existe"