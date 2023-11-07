from app.use_case.pago_filtro_rut.listar_pago_filtro_rut_use_case import ListarPagoFiltroRutsUseCase

class ListarPagoFiltroRutsController:
    def __init__(self, use_case: ListarPagoFiltroRutsUseCase):
        self.use_case = use_case

    def handle(self):
        result = self.use_case.execute()
        if result is None:
            return {"error": "No data found"}, 404
        else:
            return result, 200