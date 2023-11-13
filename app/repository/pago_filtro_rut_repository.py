# repository.py
from app.models.db.pago_filtro_rut_model_db import PagoFiltroRut
from app.repository.base_repository import BaseRepository
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import ObjectDeletedError
from app.database.database import get_db



class PagoFiltroRutRepository(BaseRepository):
    def __init__(self, Session):
        super().__init__(Session)

    def find_first_by_rut_and_fecha_fin_is_null(self, rut_cliente: str):
        return self.session.query(PagoFiltroRut).filter_by(rut_cliente=rut_cliente, fecha_fin=None).first()

    def save(self, pago_filtro_rut: PagoFiltroRut):
        self.session.add(pago_filtro_rut)
        self.session.commit()
        pago_filtro_rut_dict = pago_filtro_rut.to_dict()  # Convertir a diccionario
        return pago_filtro_rut_dict  # Devolver el diccionario
    