from typing import Annotated
from fastapi import APIRouter, Depends
from services.room_service import RoomService, get_room_service

router = APIRouter()


@router.get("/")
async def get_all(room_service: Annotated[RoomService, Depends(get_room_service)]):
    return await room_service.get_all()
