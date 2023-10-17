from fastapi import APIRouter, HTTPException
from app.models.models import PaymentParameter
from app.use_cases.payment_parameter_use_case import PaymentParameterUseCase  

router = APIRouter()

# Ruta para obtener todos los parámetros de pago
@router.get("/listarParametros")
async def get_payment_parameters() -> list:
    payment_parameters = payment_parameter_use_case.get_all_payment_parameters()
    if not payment_parameters:
        raise HTTPException(status_code=404, detail="Payment parameters not found")
    return payment_parameters
