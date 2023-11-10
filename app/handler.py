from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.controllers.channels.busqueda_canal_controller import BusquedaCanalController
from app.repository.canales_repository import CanalesRepository
from app.use_case.canales.busqueda_canal_use_case import BusquedaCanalUseCase
from app.controllers.channels.listar_canales_controller import ListarCanalesController

from app.use_case.canales.listar_canales_use_case import ListarCanalesUseCase
from app.controllers.channels.listar_canales_by_id_trx_controller import ListarCanalesByIdTrxController

from app.use_case.canales.listar_canales_by_id_trx_use_case import ListarCanalesByIdTrxUseCase
from app.controllers.channels.agrega_canal_controller import AgregaCanalController

from app.use_case.canales.agrega_canal_use_case import AgregaCanalUseCase
from app.use_case.canales.eliminar_canal_use_case import EliminarCanalUseCase   
from app.controllers.channels.eliminar_canal_controller import EliminarCanalController

from app.controllers.parametros_pago.listar_parametros_pago_controller import ListarParametrosPagoController
from app.use_case.parametros_pago.listar_parametros_pago_use_case import ListarParametrosUseCase
from app.repository.parametros_pago_repository import ParametrosPagoRepository

from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.database import get_db

from app.controllers.parametros_pago.agrega_parametros_pago_controller import AgregaParametrosPagoController
from app.use_case.parametros_pago.agrega_parametros_pago_use_case import AgregaParametrosPagoUseCase
from app.repository.parametros_pago_repository import ParametrosPagoRepository
from app.models.parametros_pago_to_model import ParametrosPagoTO

from app.controllers.parametros_pago.eliminar_parametros_pago_controller import EliminaParametrosPagoController
from app.use_case.parametros_pago.elimina_parametros_pago_use_case import EliminaParametrosPagoUseCase
from app.repository.parametros_pago_repository import ParametrosPagoRepository
from app.models.parametros_pago_to_model import ParametrosPagoTO

from app.controllers.pago_filtro_rut.pago_filtro_rut import PagoFiltroRutController
from app.use_case.pago_filtro_rut.pago_filtro_rut_use_case import PagoFiltroRutUseCase
from app.repository.pago_filtro_rut_repository import PagoFiltroRutRepository

from app.controllers.pago_filtro_rut.listar_pago_filtro_rut import ListarPagoFiltroRutsController
from app.use_case.pago_filtro_rut.listar_pago_filtro_rut_use_case import ListarPagoFiltroRutsUseCase

from app.controllers.configuracion_pago_online.configuracion_pago_online import AgregarConfiguracionPagoOnlineController
from app.use_case.configuracion_pago_online.configuracion_pago_online_use_case import AgregarConfiguracionPagoOnlineUseCase
from app.repository.configuracion_pago_online_repository import ConfiguracionPagoOnlineRepository
from app.models.configuracion_pago_online_to_model import ConfiguracionPagoOnlineTO

from app.controllers.configuracion_pago_online.obtener_configuracion_pago_online import ObtenerConfiguracionPagoOnlineController
from app.use_case.configuracion_pago_online.obtener_configuracion_pago_online import ObtenerConfiguracionPagoOnlineUseCase

from app.controllers.configuracion_pago_online.eliminar_configuracion_pago_online_controller import EliminaConfiguracionPagoOnlineController
from app.use_case.configuracion_pago_online.eliminar_configuracion_pago_online_use_case import EliminaConfiguracionPagoOnlineUseCase

from app.controllers.configuracion_pago_online.eliminar_toda_configuracion_pago_online_controller import EliminaConfiguracionPagoOnlineCompletaController
from app.use_case.configuracion_pago_online.eliminar_toda_configuracion_pago_online_use_case import EliminaConfiguracionPagoOnlineCompletaUseCase

from app.controllers.configuracion_pago_online.find_all_configuracion_pago_online_controller import ListadoConfiguracionPagoOnlineController
from app.use_case.configuracion_pago_online.find_all_configuracion_pago_online_use_case import ListadoConfiguracionPagoOnlineUseCase


app = FastAPI()

# Search channel endpoint
@app.post("/buscaCanal")
async def busca_canal(busqueda_canal: dict):
    try:
        # Create channel repository instance
        canales_repository = CanalesRepository()
        
        # Create use case instance for searching channels
        busqueda_canal_use_case = BusquedaCanalUseCase(canales_repository)
        
        # Create controller instance for handling channel search
        busqueda_canal_controller = BusquedaCanalController(busqueda_canal_use_case)
        
        # Invoke channel search using the controller
        response = busqueda_canal_controller.buscar_canal(busqueda_canal)
        
        # Return successful search response with 200 status code
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        # Return error response with 500 status code if exception occurs
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

# Start GET route
@app.get("/listarCanales")
async def listar_canales():
    try:
        # Initialize canales repository
        canales_repository = CanalesRepository()
        
        # Initialize use case for listing channels
        listar_canales_use_case = ListarCanalesUseCase(canales_repository)
        
        # Initialize controller for listing channels
        listar_canales_controller = ListarCanalesController(listar_canales_use_case)
        
        # Call controller to list channels
        response = listar_canales_controller.listar_canales()
        
        # Return response with 200 status code
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        # Return error response with 500 status code
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/listarCanalesByIdTrx")
async def listar_canales_by_id_trx(listar_canales_by_id_trx: dict):
    """ Listar canales por ID de transacción """
    try:
        # Crear repositorio de canales
        canales_repository = CanalesRepository()
        
        # Crear caso de uso de listar canales por ID de transacción
        listar_canales_by_id_trx_use_case = ListarCanalesByIdTrxUseCase(canales_repository)
        
        # Crear controlador de listar canales por ID de transacción
        listar_canales_by_id_trx_controller = ListarCanalesByIdTrxController(listar_canales_by_id_trx_use_case)
        
        # Listar canales por ID de transacción
        response = listar_canales_by_id_trx_controller.listar_canales_by_id_trx(listar_canales_by_id_trx)
        
        # Retornar respuesta con código de estado 200
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        # Retornar error con código de estado 500
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
# POST method for adding a new channel
@app.post("/agregaCanal")
async def agrega_canal(canal_to: dict):
    try:
        # Initialize CanalesRepository for handling database operations
        canales_repository = CanalesRepository()
        
        # Create AgregaCanalUseCase instance with CanalesRepository dependency
        agrega_canal_use_case = AgregaCanalUseCase(canales_repository)
        
        # Create AgregaCanalController instance with AgregaCanalUseCase dependency
        agrega_canal_controller = AgregaCanalController(agrega_canal_use_case)
        
        # Call controller method to add new channel and return JSON response
        response = agrega_canal_controller.agrega_canal(canal_to)
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        # If an error occurs, return JSON response with error details
        return JSONResponse(content={"error": str(e)}, status_code=500)

# define delete route for channel
@app.delete("/eliminarCanal")
async def eliminar_canal(canal_to: dict):
    try:
        # initialize repository
        canales_repository = CanalesRepository()
        
        # initialize use case with repository
        eliminar_canal_use_case = EliminarCanalUseCase(canales_repository)
        
        # initialize controller with use case
        eliminar_canal_controller = EliminarCanalController(eliminar_canal_use_case)
        
        # call controller method to delete channel
        response = eliminar_canal_controller.eliminar_canal(canal_to)
        
        return JSONResponse(content=response, status_code=200)
    except SQLAlchemyError as e:
        # If a SQLAlchemy error occurs, return JSON response with specific error details
        return JSONResponse(content={"error": f"Error de SQLAlchemy: {e}"}, status_code=500)
    except HTTPException as e:
        # If a HTTPException error occurs, return JSON response with specific error details
        return JSONResponse(content={"error": e.detail}, status_code=e.status_code)
    except Exception as e:
        # If an unknown error occurs, return JSON response with generic error details
        return JSONResponse(content={"error": str(e) or "Ocurrió un error desconocido"}, status_code=500)
    

@app.get("/listarParametros")
async def listar_parametros(db: Session = Depends(get_db)):
    try:
        # Get parametros_pago repository
        parametros_pago_repository = ParametrosPagoRepository(db)
        
        # Create listar_parametros_pago use case
        listar_parametros_pago_use_case = ListarParametrosUseCase(parametros_pago_repository)
        
        # Create listar_parametros_pago controller
        listar_parametros_pago_controller = ListarParametrosPagoController(listar_parametros_pago_use_case)
        
        # List parameters
        response = listar_parametros_pago_controller.listar_parametros()
        
        # Return parameters as JSON response
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        # Return error response if any exception occurs
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/agregaParametrosPago")
async def agrega_parametros_pago(parametros_pago_to: ParametrosPagoTO, db: Session = Depends(get_db)):
    try:
        # Repository pattern
        parametros_pago_repository = ParametrosPagoRepository(db)
        
        # Use case pattern
        agrega_parametros_pago_use_case = AgregaParametrosPagoUseCase(parametros_pago_repository)
        
        # Controller pattern
        agrega_parametros_pago_controller = AgregaParametrosPagoController(agrega_parametros_pago_use_case)
        
        # Invoke controller
        response = agrega_parametros_pago_controller.agrega_parametros(parametros_pago_to)
        
        # Return response as JSON
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        # Handle exception
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.delete("/eliminaParametrosPago")
async def elimina_parametros_pago(parametros_pago_to: ParametrosPagoTO, db: Session = Depends(get_db)):
    """ Delete parameter for payment. """
    try:
        parametros_pago_repository = ParametrosPagoRepository(db)
        """ Parameters payment repository. """
        elimina_parametros_pago_use_case = EliminaParametrosPagoUseCase(parametros_pago_repository)
        """ Use case for deleting parameters payment. """
        elimina_parametros_pago_controller = EliminaParametrosPagoController(elimina_parametros_pago_use_case)
        """ Controller for deleting parameters payment. """
        response = elimina_parametros_pago_controller.elimina_parametros(parametros_pago_to)
        """ Call the controller method for deleting parameters payment. """
        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        """ Handle exceptions during the operation. """
        return JSONResponse(content={"error": str(e)}, status_code=500)


# Define the pagoFiltroRut route
@app.post("/pagoFiltroRut")
async def pago_filtro_rut(pago_filtro_rut: dict):
    """ Handles POST requests for RUT filtered payments. """
    try:
        # Initialize repositories, use cases, and controllers
        pago_filtro_rut_repository = PagoFiltroRutRepository()
        pago_filtro_rut_use_case = PagoFiltroRutUseCase(pago_filtro_rut_repository)
        pago_filtro_rut_controller = PagoFiltroRutController(pago_filtro_rut_use_case)

        # Call controller method for handling the request
        response = pago_filtro_rut_controller.pago_filtro_rut(pago_filtro_rut)

        # Return the JSON response with status code 200
        return JSONResponse(content=response, status_code=200)

    except Exception as e:
        # In case of an error, return a JSON response with status code 500
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

@app.get("/pagoFiltroRut")
async def listar_pago_filtro_ruts(db: Session = Depends(get_db)):
    try:
        # Repository instance
        pago_filtro_rut_repository = PagoFiltroRutRepository(db)
        
        # Use case instance
        listar_pago_filtro_ruts_use_case = ListarPagoFiltroRutsUseCase(pago_filtro_rut_repository)
        
        # Controller instance
        listar_pago_filtro_ruts_controller = ListarPagoFiltroRutsController(listar_pago_filtro_ruts_use_case)
        
        # Handle controller request
        response, status_code = listar_pago_filtro_ruts_controller.handle()
        
        # Return JSON response
        return JSONResponse(content=response, status_code=status_code)
    except Exception as e:
        # Return JSON error response
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.post("/portal/configuracion/{id}")
async def agregar_configuracion_pago_online(configuracion_pago_online_to: ConfiguracionPagoOnlineTO, id: int, db: Session = Depends(get_db)):
    try:
        # Repository pattern
        configuracion_pago_online_repository = ConfiguracionPagoOnlineRepository(db)
        
        # Use case pattern
        agregar_configuracion_pago_online_use_case = AgregarConfiguracionPagoOnlineUseCase(configuracion_pago_online_repository)
        
        # Controller pattern
        agregar_configuracion_pago_online_controller = AgregarConfiguracionPagoOnlineController(agregar_configuracion_pago_online_use_case)
        
        # Handle request
        response, status_code = agregar_configuracion_pago_online_controller.handle(configuracion_pago_online_to, id)
        
        # Return response
        return JSONResponse(content=response, status_code=status_code)
    except Exception as e:
        # Handle error
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

@app.get("/portal/configuracion/{id}")
async def obtener_configuracion_pago_online(id: int, db: Session = Depends(get_db)):
    try:
        # create repository instance
        configuracion_pago_online_repository = ConfiguracionPagoOnlineRepository(db)
        
        # create use case instance
        obtener_configuracion_pago_online_use_case = ObtenerConfiguracionPagoOnlineUseCase(configuracion_pago_online_repository)
        
        # create controller instance
        obtener_configuracion_pago_online_controller = ObtenerConfiguracionPagoOnlineController(obtener_configuracion_pago_online_use_case)
        
        # handle controller request
        response, status_code = obtener_configuracion_pago_online_controller.handle(id)
        
        # return response as JSON
        return JSONResponse(content=response, status_code=status_code)
    except Exception as e:
        # handle any exceptions
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

@app.get("/portal/configuracion")
async def listado_configuracion_pago_online(db: Session = Depends(get_db)):
    """ Listado de configuraciones """
    try:
        configuracion_pago_online_repository = ConfiguracionPagoOnlineRepository(db)
        # Listado de configuraciones de pago online
        listado_configuracion_pago_online_use_case = ListadoConfiguracionPagoOnlineUseCase(configuracion_pago_online_repository)
        # Controller de listado de configuraciones de pago online
        listado_configuracion_pago_online_controller = ListadoConfiguracionPagoOnlineController(listado_configuracion_pago_online_use_case)
        # Ejecutar la solicitud
        response, status_code = listado_configuracion_pago_online_controller.handle()
        # Retornar la respuesta con su respectivo status code
        return JSONResponse(content=response, status_code=status_code)
    except Exception as e:
        # Manejar excepciones
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

@app.delete("/portal/configuracion/{id}")
async def elimina_configuracion_pago_online(id: int, db: Session = Depends(get_db)):
    try:
        # Get configuracion pago online repository
        configuracion_pago_online_repository = ConfiguracionPagoOnlineRepository(db)
        
        # Create use case for eliminating configuracion pago online
        elimina_configuracion_pago_online_use_case = EliminaConfiguracionPagoOnlineUseCase(configuracion_pago_online_repository)
        
        # Create controller for handling elimination request
        elimina_configuracion_pago_online_controller = EliminaConfiguracionPagoOnlineController(elimina_configuracion_pago_online_use_case)
        
        # Handle elimination request
        response, status_code = elimina_configuracion_pago_online_controller.handle(id)
        return JSONResponse(content=response, status_code=status_code)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

@app.delete("/portal/configuracion/eliminar/{id}")
async def elimina_configuracion_pago_online_completa(id: int, db: Session = Depends(get_db)):
    try:
        # Get repository
        configuracion_pago_online_repository = ConfiguracionPagoOnlineRepository(db)
        
        # Get use case
        elimina_configuracion_pago_online_completa_use_case = EliminaConfiguracionPagoOnlineCompletaUseCase(configuracion_pago_online_repository)
        
        # Get controller
        elimina_configuracion_pago_online_completa_controller = EliminaConfiguracionPagoOnlineCompletaController(elimina_configuracion_pago_online_completa_use_case)
        
        # Handle request
        response, status_code = elimina_configuracion_pago_online_completa_controller.handle(id)
        return JSONResponse(content=response, status_code=status_code)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)