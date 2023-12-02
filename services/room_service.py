from typing import Annotated
from fastapi import Depends
from repository.room_repository import RoomRepository, get_room_repository

class RoomService():
    def __init__(self, room_repo: RoomRepository):
        self.room_repo: RoomRepository = room_repo

    async def get_all(self):
        return await self.room_repo.find_all()

def get_room_service(room_repo: Annotated[RoomRepository, Depends(get_room_repository)]):
    return RoomService(room_repo)