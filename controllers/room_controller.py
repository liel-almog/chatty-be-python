from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from services.room_service import RoomService, get_room_service
from services.message_service import MessageService, get_message_service
from models.room_model import RoomModel
from models.message_model import MessageModel

router = APIRouter()


@router.get("/", response_model=list[RoomModel])
async def get_all(room_service: Annotated[RoomService, Depends(get_room_service)]):
    return await room_service.get_all()


@router.get("/{room_id}/message", response_model=list[MessageModel] | None)
async def get_all_messages_by_room_id(
    room_id: int,
    room_service: Annotated[RoomService, Depends(get_room_service)],
    message_service: Annotated[MessageService, Depends(get_message_service)],
):
    room = await room_service.get_one(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    return await message_service.get_all_by_room(room_id)
