from fastapi import APIRouter, HTTPException
from typing import List
from app.models.channel import Channel, BusquedaCanal
from app.use_cases.channel_use_case import ChannelUseCase  

router = APIRouter()

# Instancia el use case
channel_use_case = ChannelUseCase()

# Ruta para obtener todos los canales por idTrx
@router.post("/listarCanalesByIdTrx")
async def get_channels_by_idTrx(idTrx: int) -> List[Channel]:
    channels = channel_use_case.get_channels_by_idTrx(idTrx)
    if not channels:
        raise HTTPException(status_code=404, detail="Channels not found")
    return channels