from app.models.canales_model import Canales
from app.repository.canales_repository import CanalesRepository

class BusquedaCanalUseCase:
    def __init__(self, canales_repository: CanalesRepository):
        self.canales_repository = canales_repository

    def buscar_canal(self, idCanal= None, producto=None, idConvenio=None, tipoOrigen=None, tipoSeguro=None, tipoProducto=None, idEmpresa=None, passwordCanal=None):
        canal = self.canales_repository.buscar_canal(idCanal, producto, idConvenio, tipoOrigen, tipoSeguro, tipoProducto, idEmpresa, passwordCanal)
        if canal is None:
            raise Exception("Canal no encontrado")
        return canal