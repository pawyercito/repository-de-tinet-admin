from app.use_case.canales.agrega_canal_use_case import AgregaCanalUseCase

class AgregaCanalController:
    def __init__(self, agrega_canal_use_case: AgregaCanalUseCase):
        self.agrega_canal_use_case = agrega_canal_use_case

    def agrega_canal(self, canal_to: dict):
        try:
            canal_data = {
                "tipoSeguro": canal_to.get("tipoSeguro"),
                "tipoOrigen": canal_to.get("tipoOrigen"),
                "producto": canal_to.get("producto"),
                "idConvenio": canal_to.get("idConvenio"),
                "tipoProducto": canal_to.get("tipoProducto"),
                "passwordCanal": canal_to.get("passwordCanal"),
                "idEmpresa": canal_to.get("idEmpresa"),
                "idCanal": canal_to.get("idCanal"),
                "descripcion": canal_to.get("descripcion")
            }
            response = self.agrega_canal_use_case.agrega_canal(canal_data)
            return response
        except Exception as e:
            return {"error": str(e)}