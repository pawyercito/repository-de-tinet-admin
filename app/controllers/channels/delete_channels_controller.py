from fastapi import APIRouter, HTTPException
from typing import List
from app.models.channel import Channel, BusquedaCanal
from app.use_cases.channel_use_case import ChannelUseCase  

router = APIRouter()

# Instancia el use case
channel_use_case = ChannelUseCase()

# Ruta para eliminar un canal
@router.delete("/eliminarCanal{id}")
async def delete_channel(id: int) -> Channel:
    channel_db = channel_use_case.get_channel(id)
    if not channel_db:
        raise HTTPException(status_code=404, detail="Channel not found")
    channel_use_case.delete_channel(id)
    return channel_db