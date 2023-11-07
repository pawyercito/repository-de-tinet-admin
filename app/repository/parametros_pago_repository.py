from sqlalchemy.orm import Session
from app.models.db.parametros_pago_model_db import ParametrosPago
from app.models.parametros_pago_model import ParametrosPago as ParametrosPagoModel
from app.repository.base_repository import BaseRepository

class ParametrosPagoRepository(BaseRepository):

    def listar_parametros(self):
        parametros = self.db.query(ParametrosPago).all()
        return [parametro.__dict__ for parametro in parametros]
    
    def save(self, parametros_pago: ParametrosPago):
        self.db.add(parametros_pago)
        self.db.commit()

    def exists(self, claves):
        return self.db.query(ParametrosPago).filter_by(claves=claves).first() is not None
    
    def delete(self, claves):
        parametros_pago = self.db.query(ParametrosPago).filter_by(claves=claves).first()
        if parametros_pago:
            self.db.delete(parametros_pago)
            self.db.commit()
    

    