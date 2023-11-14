from app.use_case.pago_filtro_rut.listar_pago_filtro_rut_use_case import ListarPagoFiltroRutsUseCase
from datetime import datetime

class ListarPagoFiltroRutsController:
    def __init__(self, use_case: ListarPagoFiltroRutsUseCase):
        self.use_case = use_case

    def handle(self):
        result = self.use_case.execute()
        if result is None:
            return {"error": "No se consiguio ningun pago filtro rut"}, 404
        else:
            return [
                {
                    key: value.isoformat() if isinstance(value, datetime) else value
                    for key, value in item.items()
                }
                for item in result
            ], 200