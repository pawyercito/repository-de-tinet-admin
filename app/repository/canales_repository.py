from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.models.db.canales_model_db import Canales
from app.models.canales_model import Canales as CanalesModel    
from app.repository.base_repository import BaseRepository
import logging
import pdb
from sqlalchemy import and_, or_, null



# Configura el sistema de registros
logging.basicConfig(filename='app.log', level=logging.DEBUG)

class CanalesRepository(BaseRepository):
    
    def buscar_canal(self, idCanal=None, producto=None, idConvenio=None, tipoOrigen=None, tipoSeguro=None, tipoProducto=None, idEmpresa=None, passwordCanal=None):
        # Start with a query for all rows
        query = self.session.query(Canales)
        # Add conditions for each parameter that is not None
        if idCanal is not None:
            query = query.filter(Canales.idCanal == idCanal)
        if producto is not None:
            query = query.filter(Canales.producto == producto)
        if idConvenio is not None:
            query = query.filter(Canales.idConvenio == idConvenio)
        if tipoOrigen is not None:
            query = query.filter(Canales.tipoOrigen == tipoOrigen)
        if tipoSeguro is not None:
            query = query.filter(Canales.tipoSeguro == tipoSeguro)
        if tipoProducto is not None:
            query = query.filter(Canales.tipoProducto == tipoProducto)
        if idEmpresa is not None:
            query = query.filter(Canales.idEmpresa == idEmpresa)
        if passwordCanal is not None:
            query = query.filter(Canales.passwordCanal == passwordCanal)

        # Execute the query and return the result
        canal = query.first()
        if canal is not None:
            return canal.to_dict()
        else:
            return None
    
    def obtener_todos_los_canales(self):
        canales = self.session.query(Canales).all()
        logging.info(f"Canales obtenidos de la consulta: {canales}")
        if canales is None:
            return None
        return [canal.__dict__ for canal in canales]
    
    def buscar_canales_por_id_trx_y_nro_orden(self, id_trx, nro_orden):
        canales = self.session.query(Canales).filter_by(id_trx=id_trx).all()
        if canales is None:
            return None
        return [canal.__dict__ for canal in canales]
    
    def existe_canal(self, producto, id_convenio, tipo_origen, tipo_seguro):
        canal = self.session.query(Canales).filter_by(producto=producto, id_convenio=id_convenio, tipo_origen=tipo_origen, tipo_seguro=tipo_seguro).first()
        if canal is None:
            return False
        return True
    
    def guardar_canal(self, canal):
        self.session.add(canal)
        self.session.commit()
        return canal.__dict__
    
    def eliminar_canal(self, canal: CanalesModel):
        canal_db = self.db.query(Canales).filter_by(
            producto=canal.producto,
            id_convenio=canal.id_convenio,
            tipo_origen=canal.tipo_origen,
            tipo_seguro=canal.tipo_seguro
        ).first()
        if canal_db is None:
            return "El registro no existe"
        self.db.delete(canal_db)
        self.db.commit()
        return "Se eliminó correctamente"
        