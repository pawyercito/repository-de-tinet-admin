from app.repository.canales_repository import CanalesRepository

class AgregaCanalUseCase:
    def __init__(self, canales_repository: CanalesRepository):
        self.canales_repository = canales_repository

    def agrega_canal(self, canal_data: dict):
        # Verifica si el canal ya existe antes de intentar guardarlo
        if self.canales_repository.existe_canal(**canal_data):
            raise Exception("El canal ya existe y no se puede agregar nuevamente.")
        
        return self.canales_repository.guardar_canal(canal_data)