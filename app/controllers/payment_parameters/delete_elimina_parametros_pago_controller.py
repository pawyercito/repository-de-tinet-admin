from fastapi import APIRouter, HTTPException
from app.models.models import PaymentParameter
from app.use_cases.payment_parameter_use_case import PaymentParameterUseCase  # Importa el use case

router = APIRouter()

# Instancia el use case
payment_parameter_use_case = PaymentParameterUseCase()

# Ruta para eliminar un parámetro de pago
@router.delete("/eliminaParametrosPago")
async def elimina_parametros_pago(parametros_pago_to: ParametrosPagoTO, 
                                  parametros_pago_use_case: ParametrosPagoUseCase = Depends(ParametrosPagoUseCase(ParametrosPagoRepository()))):
    return await parametros_pago_use_case.elimina_parametros_pago(parametros_pago_to)