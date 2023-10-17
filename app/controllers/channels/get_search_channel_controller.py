from fastapi import APIRouter, HTTPException
from typing import List
from app.models.channel import Channel, BusquedaCanal
from app.use_cases.channel_use_case import ChannelUseCase  

router = APIRouter()

# Instancia el use case
channel_use_case = ChannelUseCase()

# Ruta para obtener todos los canales
@router.get("/listarCanales")
async def get_channels() -> List[Channel]:
    channels = channel_use_case.get_channels()
    if not channels:
        raise HTTPException(status_code=404, detail="Channels not found")
    return channels