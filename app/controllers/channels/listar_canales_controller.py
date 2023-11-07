from app.use_case.canales.listar_canales_use_case import ListarCanalesUseCase

class ListarCanalesController:
    def __init__(self, listar_canales_use_case: ListarCanalesUseCase):
        self.listar_canales_use_case = listar_canales_use_case

    def listar_canales(self):
        canales = self.listar_canales_use_case.listar_canales()
        return canales