from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.db.configuracion_pago_online_db_model import ConfiguracionPagoOnline
from datetime import datetime
from sqlalchemy.orm.session import Session
from app.repository.base_repository import BaseRepository
from typing import Optional

import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

class ConfiguracionPagoOnlineRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)

    def exists(self, id: int):
        return self.session.query(ConfiguracionPagoOnline).filter(ConfiguracionPagoOnline.id == id).first() is not None

    def save(self, configuracion_pago_online: ConfiguracionPagoOnline):
        self.session.add(configuracion_pago_online)
        self.session.commit()
        self.session.refresh(configuracion_pago_online)
        return configuracion_pago_online

    def findOne(self, id: int):
        return self.session.query(ConfiguracionPagoOnline).filter(ConfiguracionPagoOnline.id == id).first()

    def actualizarConfiguracionPago(self, id: int, glosa: str, valor: str, deffecdate: datetime):
        configuracion_pago_online = self.findOne(id)
        configuracion_pago_online.glosa = glosa
        configuracion_pago_online.valor = valor
        configuracion_pago_online.deffecdate = deffecdate
        self.session.commit()
        return configuracion_pago_online

    def listado_pago(self, id: int) -> Optional[ConfiguracionPagoOnline]:
        return self.session.query(ConfiguracionPagoOnline).filter(ConfiguracionPagoOnline.id == id).first()
        
    def find_all(self):
        return self.session.query(ConfiguracionPagoOnline).all()
    
    def eliminar_configuracion_pago(self, id: int):
        configuracion_pago_online = self.session.query(ConfiguracionPagoOnline).filter(ConfiguracionPagoOnline.id == id).first()
        if configuracion_pago_online is not None:
            self.session.delete(configuracion_pago_online)
            self.session.commit()
            return True
        else:
            return False
        
    def eliminar_configuracion_pago_completo(self, id: int):
        configuracion_pago_online = self.session.query(ConfiguracionPagoOnline).filter(ConfiguracionPagoOnline.id == id).first()
        if configuracion_pago_online is not None:
            self.session.delete(configuracion_pago_online)
            self.session.commit()
            return True
        else:
            return False    