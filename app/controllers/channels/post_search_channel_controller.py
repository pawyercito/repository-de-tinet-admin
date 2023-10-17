from fastapi import APIRouter, HTTPException
from typing import List
from app.models.busqueda_canal_to_model import BusquedaCanalTO
from app.use_cases.channel_use_case import ChannelUseCase  

router = APIRouter()

# Instancia el use case
channel_use_case = ChannelUseCase()

# Ruta para obtener un solo canal
@router.post("/buscaCanal", response_model=List[Channel])
async def search_channel(busqueda: BusquedaCanalTO) -> List[Channel]:
    channel = channel_use_case.search_channel(busqueda)
    if not channel:
        raise HTTPException(status_code=404, detail="No channels found")
    return channel
