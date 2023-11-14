from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from app.models.db.canales_model_db import Canales
from app.models.canales_model import Canales as CanalesModel    
from app.repository.base_repository import BaseRepository
import logging
import pdb
from sqlalchemy import and_, or_, null
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session



# Configura el sistema de registros
logging.basicConfig(filename='app.log', level=logging.DEBUG)

class CanalesRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db)
    
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
    
    def existe_canal(self, idCanal, descripcion, producto, idConvenio, tipoOrigen, tipoSeguro, tipoProducto, idEmpresa, passwordCanal):
        # Realiza una consulta para verificar si el canal ya existe en la base de datos
        existing_canal = self.session.query(Canales).filter_by(
            idCanal=idCanal,
            descripcion=descripcion,
            producto=producto,
            idConvenio=idConvenio,
            tipoOrigen=tipoOrigen,
            tipoSeguro=tipoSeguro,
            tipoProducto=tipoProducto,
            idEmpresa=idEmpresa,
            passwordCanal=passwordCanal
        ).first()

        return existing_canal is not None

    def guardar_canal(self, canal_data: Canales):
        # Verifica si el canal ya existe
        if self.existe_canal(**canal_data):
            raise Exception("El canal ya existe y no se puede agregar nuevamente.")
        
        # Si el canal no existe, crea y guarda el nuevo canal
        new_canal = Canales(**canal_data)
        try:
            self.session.add(new_canal)
            self.session.commit()
            return "Se agregó correctamente"
        except SQLAlchemyError as e:
            self.session.rollback()
            error = str(e.__dict__['orig'])
            return f"Error: {error}"
    
    def eliminar_canal(self, idCanal, descripcion, producto, idConvenio, tipoOrigen, tipoSeguro, tipoProducto, idEmpresa, passwordCanal):
    # Verifica si el canal ya existe
        if not self.existe_canal(idCanal, descripcion, producto, idConvenio, tipoOrigen, tipoSeguro, tipoProducto, idEmpresa, passwordCanal):
            raise Exception("El canal no existe y no se puede eliminar.")
        # Si el canal existe, elimina del sistema
        try:
            self.session.query(Canales).filter_by(
                idCanal=idCanal,
                descripcion=descripcion,
                producto=producto,
                idConvenio=idConvenio,
                tipoOrigen=tipoOrigen,
                tipoSeguro=tipoSeguro,
                tipoProducto=tipoProducto,
                idEmpresa=idEmpresa,
                passwordCanal=passwordCanal
            ).delete()
            self.session.commit()
            return {"message": "Canal eliminado correctamente"}
        except SQLAlchemyError as e:
            self.session.rollback()
            error = str(e.__dict__['orig'])
            return {"error": f"Error: {error}"}
        
        