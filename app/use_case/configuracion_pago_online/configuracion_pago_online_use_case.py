from app.models.db.configuracion_pago_online_db_model import ConfiguracionPagoOnline
from app.models.configuracion_pago_online_to_model import ConfiguracionPagoOnlineTO
from app.repository.configuracion_pago_online_repository import ConfiguracionPagoOnlineRepository
from datetime import datetime
class AgregarConfiguracionPagoOnlineUseCase:
    def __init__(self, repository: ConfiguracionPagoOnlineRepository):
        self.repository = repository

    def execute(self, configuracion_pago_online_to: ConfiguracionPagoOnlineTO, id: int):
        if configuracion_pago_online_to.glosa is None or configuracion_pago_online_to.valor is None:
            return None

        configuracion_pago_online = ConfiguracionPagoOnline()
        configuracion_pago_online.id = id
        configuracion_pago_online.glosa = configuracion_pago_online_to.glosa
        configuracion_pago_online.valor = configuracion_pago_online_to.valor

        if configuracion_pago_online_to.deffecdate is None:
            configuracion_pago_online.deffecdate = datetime.utcnow()
        else:
            configuracion_pago_online.deffecdate = configuracion_pago_online_to.deffecdate

        if not self.repository.exists(id):
            return self.repository.save(configuracion_pago_online)
        else:
            configuracion = self.repository.findOne(id)
            if configuracion.deffecdate is not None:
                return self.repository.actualizarConfiguracionPago(id, configuracion_pago_online.glosa, configuracion_pago_online.valor, configuracion_pago_online.deffecdate)
            else:
                return None