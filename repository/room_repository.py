from typing import Annotated
from databases import Database
from database.db import get_db
from fastapi import Depends

class RoomRepository:
    def __init__(self, db: Database):
        self.db = db

    # Create a route to return all rooms
    async def find_all(self):
        return await self.db.fetch_all("SELECT * FROM public.rooms")

def get_room_repository(db: Annotated[Database, Depends(get_db)]):
    return RoomRepository(db)