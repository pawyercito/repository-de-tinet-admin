from app.use_case.canales.listar_canales_by_id_trx_use_case import ListarCanalesByIdTrxUseCase
from app.models.listar_canales_by_id_trx_nro_orden import ListarCanalesByIdTrxNroOrdenTO
class ListarCanalesByIdTrxController:
    def __init__(self, listar_canales_by_id_trx_use_case: ListarCanalesByIdTrxUseCase):
        self.listar_canales_by_id_trx_use_case = listar_canales_by_id_trx_use_case

    def listar_canales_by_id_trx(self, listar_canales_by_id_trx: ListarCanalesByIdTrxNroOrdenTO):
        id_trx = listar_canales_by_id_trx.idTrx
        nro_orden = listar_canales_by_id_trx.nroOrden
        canales = self.listar_canales_by_id_trx_use_case.listar_canales_by_id_trx(id_trx, nro_orden)
        return canales