from app.repository.canales_repository import CanalesRepository

class AgregaCanalUseCase:
    def __init__(self, canales_repository: CanalesRepository):
        self.canales_repository = canales_repository

    def agrega_canal(self, canal):
        if self.canales_repository.existe_canal(canal):
            return "El registro ya existe"
        else:
            self.canales_repository.guardar_canal(canal)
            return "Se agregó correctamente"