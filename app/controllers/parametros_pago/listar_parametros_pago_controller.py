from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.parametros_pago_model import ParametrosPago
from app.use_case.parametros_pago.listar_parametros_pago_use_case import ListarParametrosUseCase
from app.repository.parametros_pago_repository import ParametrosPagoRepository

router = APIRouter()


class ListarParametrosPagoController:
    def __init__(self, use_case: ListarParametrosUseCase):
        self.use_case = use_case

    def listar_parametros(self):
        return self.use_case.listar_parametros()