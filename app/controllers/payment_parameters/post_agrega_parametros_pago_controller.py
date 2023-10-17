from fastapi import APIRouter, HTTPException
from app.models.models import PaymentParameter
from app.use_cases.payment_parameter_use_case import PaymentParameterUseCase  # Importa el use case

router = APIRouter()

# Instancia el use case
payment_parameter_use_case = PaymentParameterUseCase()

# Ruta para agregar parámetros de pago
@router.post("/agregaParametrosPago")
async def add_payment_parameter(payment_parameter: PaymentParameter) -> PaymentParameter:
    return payment_parameter_use_case.add_payment_parameter(payment_parameter)





