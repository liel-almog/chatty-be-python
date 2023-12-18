from typing import Annotated
from databases import Database
from fastapi import Depends

from database.db import CommonDB


class RoomService:
    def __init__(self, db: Database):
        self.db = db

    async def get_all(self):
        return await self.db.fetch_all("SELECT id, name, created_at FROM public.rooms")

    async def get_one(self, room_id: int):
        return await self.db.fetch_one(
            "SELECT id, name, created_at FROM public.rooms WHERE id = :id",
            values={"id": room_id},
        )


def get_room_service(db: CommonDB):
    return RoomService(db)

CommonRoomService = Annotated[RoomService, Depends(get_room_service, use_cache=True)]