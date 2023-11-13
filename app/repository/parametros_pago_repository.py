from sqlalchemy.orm import Session
from app.models.db.parametros_pago_model_db import ParametrosPago
from app.models.parametros_pago_model import ParametrosPago as ParametrosPagoModel
from app.repository.base_repository import BaseRepository
import logging
class ParametrosPagoRepository(BaseRepository):

    def listar_parametros(self):
        parametros = self.session.query(ParametrosPago).all()
        logging.info(f"Parametros obtenidos de la consulta: {parametros}")
        if parametros is None:
            return None
        return [parametro.__dict__ for parametro in parametros]
       
    
    def exists(self, id_padre, id, valor, descripcion):
        # realiza una consulta para verificar si el parametro ya existe
        existing_parametros_pago = self.session.query(ParametrosPago).filter_by(
            id_padre=id_padre,
            id=id,
            valor=valor,
            descripcion=descripcion
        ).first()

        return existing_parametros_pago is not None

    def save(self, parametros_pago_data: dict):
        #verifica si ya el parametro existe
        if self.exists(**parametros_pago_data):
            raise Exception("El parametro ya existe y no se puede agregar nuevamente.")
        #si el parametro no existe, crea y guarda el nuevo parametro
        new_parametros_pago = ParametrosPago(**parametros_pago_data)
        try:
            self.session.add(new_parametros_pago)
            self.session.commit()
            return "Se agregó correctamente"
        except Exception as e:
            self.session.rollback()
            error = str(e.__dict__['orig'])
            return f"Error: {error}"   
    
    def delete(self, id_padre, id, valor, descripcion):
        #verifica si el parametro existe
        if not self.exists(id_padre, id, valor, descripcion):
            raise Exception("El parametro no existe y no se puede eliminar.")
        #si el parametro existe, elimina del sistema
        try:
            self.session.query(ParametrosPago).filter_by(
                id_padre=id_padre,
                id=id,
                valor=valor,
                descripcion=descripcion
            ).delete()
            self.session.commit()
            return "Se eliminó correctamente"
        except Exception as e:
            self.session.rollback()
            error = str(e.__dict__['orig'])
            return f"Error: {error}"
       
    

    