from app.use_case.canales.agrega_canal_use_case import AgregaCanalUseCase

class AgregaCanalController:
    def __init__(self, agrega_canal_use_case: AgregaCanalUseCase):
        self.agrega_canal_use_case = agrega_canal_use_case

    def agrega_canal(self, canal_to):
        canal = {
            "tipoSeguro": canal_to.get("tipoSeguro"),
            "tipoOirgen": canal_to.get("tipoOirgen"),
            "producto": canal_to.get("producto"),
            "idConvenio": canal_to.get("idConvenio"),
            "tipoProducto": canal_to.get("tipoProducto"),
            "passwordCanal": canal_to.get("passwordCanal"),
            "idEmpresa": canal_to.get("idEmpresa"),
            "idCanal": canal_to.get("idCanal"),
            "descripcion": canal_to.get("descripcion")
        }
        response = self.agrega_canal_use_case.agrega_canal(canal)
        return response