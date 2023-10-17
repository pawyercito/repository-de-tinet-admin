from fastapi import APIRouter, HTTPException
from typing import List
from app.models.channel import Channel, BusquedaCanal
from app.use_cases.channel_use_case import ChannelUseCase  

router = APIRouter()

# Instancia el use case
channel_use_case = ChannelUseCase()

# Ruta para agregar un canal
@router.post("/agregaCanal")
async def add_channel(channel: Channel) -> Channel:
    return channel_use_case.add_channel(channel)