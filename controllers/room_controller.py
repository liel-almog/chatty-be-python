from typing import Annotated
from fastapi import APIRouter, Depends
from services.room_service import RoomService, get_room_service
from models.room_model import RoomModel

router = APIRouter()


@router.get("/", response_model=list[RoomModel])
async def get_all(room_service: Annotated[RoomService, Depends(get_room_service)]):
    return await room_service.get_all()
