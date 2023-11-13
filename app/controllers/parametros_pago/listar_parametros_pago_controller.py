from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.parametros_pago_model import ParametrosPago
from app.use_case.parametros_pago.listar_parametros_pago_use_case import ListarParametrosUseCase


class ListarParametrosPagoController:
    def __init__(self, listar_parametros_pago_use_case: ListarParametrosUseCase):
        self.listar_parametros_pago_use_case = listar_parametros_pago_use_case

    def listar_parametros(self):
        parametros= self.listar_parametros_pago_use_case.listar_parametros()
        return parametros