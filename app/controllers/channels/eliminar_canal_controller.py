from app.use_case.canales.eliminar_canal_use_case import EliminarCanalUseCase

class EliminarCanalController:
    def __init__(self, eliminar_canal_use_case: EliminarCanalUseCase):
        self.eliminar_canal_use_case = eliminar_canal_use_case

    def eliminar_canal(self, id):
        response = self.eliminar_canal_use_case.eliminar_canal(id)
        return response