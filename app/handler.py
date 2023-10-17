from fastapi import APIRouter, HTTPException
from models.models import CanalTO, ListarCanalesByIdTrxTO, Canal, ParametrosPago, PagoTO
from business import CanalesBusiness, ParametrosPagoBusiness, PagoBusiness, ConfiguracionBusiness
from typing import List


router = APIRouter()
canalesBusiness = CanalesBusiness()
parametrosPagoBusiness = ParametrosPagoBusiness()
pagoBusiness = PagoBusiness()
configuracionBusiness = ConfiguracionBusiness()

@router.delete("/eliminarCanal")
async def eliminarCanal(canal: CanalTO):
    db_canal = canalesBusiness.buscaCanal(canal.producto, canal.idConvenio, canal.tipoOrigen, canal.tipoSeguro)
    if db_canal is None:
        raise HTTPException(status_code=404, detail="Canal no encontrado")
    canalesBusiness.eliminaCanal(db_canal)
    return {"mensaje": "Canal eliminado correctamente"}

@router.get("/buscaCanal")
async def buscaCanal(producto: str, idConvenio: int, tipoOrigen: str, tipoSeguro: str) -> Canal:
    canal = canalesBusiness.buscaCanal(producto, idConvenio, tipoOrigen, tipoSeguro)
    if canal is None:
        raise HTTPException(status_code=404, detail="Canal no encontrado")
    return canal

@router.get("/obtieneTodosLosCanales")
#Logica para obtener todos los canales
async def obtieneTodosLosCanales() -> List[Canal]:
    canales = canalesBusiness.obtieneTodosLosCanales()
    return canales

@router.post("/busquedaCanalesPorIdtrxAndNroorden")
async def busquedaCanalesPorIdtrxAndNroorden(listarCanalesByIdTrxTO: ListarCanalesByIdTrxTO) -> List[Canal]:
    canales = canalesBusiness.busquedaCanalesPorIdtrxAndNroorden(listarCanalesByIdTrxTO.idTrx, listarCanalesByIdTrxTO.nroOrden)
    return canales

@router.put("/actualizaCanal")
async def actualizaCanal(canal: CanalTO):
    db_canal = canalesBusiness.buscaCanal(canal.producto, canal.idConvenio, canal.tipoOrigen, canal.tipoSeguro)
    if db_canal is None:
        raise HTTPException(status_code=404, detail="Canal no encontrado")
    db_canal.tipoProducto = canal.tipoProducto
    db_canal.passwordCanal = canal.passwordCanal
    db_canal.idEmpresa = canal.idEmpresa
    db_canal.idCanal = canal.idCanal
    db_canal.descripcion = canal.descripcion
    canalesBusiness.actualizaCanal(db_canal)
    return {"mensaje": "Canal actualizado correctamente"}

@router.post("/parametrosPago")
async def parametrosPago(parametrosPago: ParametrosPago):
    parametrosPagoBusiness.guardarParametrosPago(parametrosPago)
    return {"mensaje": "Parámetros de pago guardados correctamente"}

@router.post("/agregaParametrosPago")
async def agregaParametrosPago(parametrosPago: ParametrosPago):
    parametrosPagoBusiness.agregarParametrosPago(parametrosPago)
    return {"mensaje": "Parámetros de pago agregados correctamente"}

@router.delete("/eliminaParametrosPago")
async def eliminaParametrosPago(parametrosPago: ParametrosPago):
    db_parametrosPago = parametrosPagoBusiness.eliminarParametrosPago(parametrosPago.id)
    if db_parametrosPago is None:
        raise HTTPException(status_code=404, detail="Parámetros de pago no encontrados")
    parametrosPagoBusiness.eliminaParametrosPago(db_parametrosPago)
    return {"mensaje": "Parámetros de pago eliminados correctamente"}

@router.get("/obtenerTodosLosParametros")
async def obtenerTodosLosParametros() -> List[ParametrosPago]:
    parametrosPago = parametrosPagoBusiness.obtenerTodosLosParametros()
    return parametrosPago

@router.put("/actualizaParametrosPago")
async def actualizaParametrosPago(parametrosPago: ParametrosPago):
    db_parametrosPago = parametrosPagoBusiness.obtenerTodosLosParametros(parametrosPago.id)
    if db_parametrosPago is None:
        raise HTTPException(status_code=404, detail="Parámetros de pago no encontrados")
    db_parametrosPago.idPadre = parametrosPago.idPadre
    db_parametrosPago.descripcion = parametrosPago.descripcion
    db_parametrosPago.valor = parametrosPago.valor
    parametrosPagoBusiness.actualizarParametrosPago(db_parametrosPago)
    return {"mensaje": "Parámetros de pago actualizados correctamente"}

@router.post("/pagoFiltroRut")
async def pagoFiltroRut(pagoTO: PagoTO):
    pagos = pagoBusiness.pagoFiltroRut(pagoTO.rut)
    return pagos

@router.get("/portal/configuracion/{id}")
async def getConfiguracion(id: int):
    configuracion = configuracionBusiness.obtenerConfiguracion(id)
    if configuracion is None:
        raise HTTPException(status_code=404, detail="Configuración no encontrada")
    return configuracion