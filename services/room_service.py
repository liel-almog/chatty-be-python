from typing import Annotated
from databases import Database
from fastapi import Depends
from database.db import get_db


class RoomService:
    def __init__(self, db: Database):
        self.db = db

    async def get_all(self):
        return await self.db.fetch_all("SELECT * FROM public.rooms")


def get_room_service(db: Annotated[Database, Depends(get_db)]):
    return RoomService(db)
