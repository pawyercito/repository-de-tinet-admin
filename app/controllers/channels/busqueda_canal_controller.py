from app.use_case.canales.busqueda_canal_use_case import BusquedaCanalUseCase

class BusquedaCanalController:
    def __init__(self, busqueda_canal_use_case: BusquedaCanalUseCase):
        self.busqueda_canal_use_case = busqueda_canal_use_case

    def buscar_canal(self, busqueda_canal):
        idCanal = busqueda_canal.get("idCanal")
        producto = busqueda_canal.get("producto")
        idConvenio = busqueda_canal.get("idConvenio")
        tipoOrigen = busqueda_canal.get("tipoOrigen")
        tipoSeguro = busqueda_canal.get("tipoSeguro")
        tipoProducto = busqueda_canal.get("tipoProducto")
        idEmpresa = busqueda_canal.get("idEmpresa")
        passwordCanal = busqueda_canal.get("passwordCanal")
            
        canales = self.busqueda_canal_use_case.buscar_canal(idCanal, producto, idConvenio, tipoOrigen, tipoSeguro, tipoProducto, idEmpresa, passwordCanal)
        if canales is not None:
            return canales
        else:
            return {"error": "Canal no encontrado"}